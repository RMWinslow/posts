"""Capture the Taxonomic Ranker OpenGraph image.

The script starts a local HTTP server for this directory, launches an installed
Chromium-family browser in headless mode, and saves a 1200x630 screenshot to
taxonomic-ranker-og.png. It uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import shutil
import socket
import struct
import subprocess
import tempfile
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_HTML = SCRIPT_DIR / "taxonomic-ranker.html"
DEFAULT_OUTPUT = SCRIPT_DIR / "taxonomic-ranker-og.png"
DEFAULT_PORT = 63201
DEFAULT_WIDTH = 1200
DEFAULT_HEIGHT = 630
DEFAULT_SETTLE_DELAY = 3


class QuietStaticHandler(SimpleHTTPRequestHandler):
    """Serve files quietly from the requested directory."""

    def log_message(self, format, *args):  # noqa: A002 - inherited API name.
        return


class LocalServer:
    def __init__(self, directory: Path, port: int, html_name: str):
        self.directory = directory
        self.port = port
        self.html_name = html_name
        self.httpd: ThreadingHTTPServer | None = None
        self.thread: threading.Thread | None = None
        self.owns_server = False

    def __enter__(self) -> "LocalServer":
        if self._existing_server_has_page(self.port):
            return self

        try:
            self._start(self.port)
            return self
        except OSError:
            self._start(find_free_port())
            return self

    def __exit__(self, exc_type, exc, tb):
        if self.httpd:
            self.httpd.shutdown()
            self.httpd.server_close()
        if self.thread:
            self.thread.join(timeout=2)

    @property
    def url(self) -> str:
        return f"http://127.0.0.1:{self.port}/{urllib.parse.quote(self.html_name)}"

    def _start(self, port: int) -> None:
        def make_handler(*args, **kwargs):
            return QuietStaticHandler(*args, directory=str(self.directory), **kwargs)

        self.httpd = ThreadingHTTPServer(("127.0.0.1", port), make_handler)
        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
        self.thread.start()
        self.port = port
        self.owns_server = True

    def _existing_server_has_page(self, port: int) -> bool:
        url = f"http://127.0.0.1:{port}/{urllib.parse.quote(self.html_name)}"
        try:
            with urllib.request.urlopen(url, timeout=1.5) as response:
                sample = response.read(4096).decode("utf-8", errors="replace")
        except (OSError, urllib.error.URLError):
            return False
        return response.status == 200 and "Taxonomic Ranker" in sample


class CdpConnection:
    def __init__(self, websocket_url: str, timeout: float = 20):
        self.websocket_url = websocket_url
        self.timeout = timeout
        self.recv_buffer = b""
        self.sock = self._open_socket(websocket_url)
        self.next_id = 1

    def __enter__(self) -> "CdpConnection":
        return self

    def __exit__(self, exc_type, exc, tb):
        try:
            self.sock.close()
        except OSError:
            pass

    def call(self, method: str, params: dict | None = None) -> dict:
        message_id = self.next_id
        self.next_id += 1
        payload = {"id": message_id, "method": method}
        if params is not None:
            payload["params"] = params
        self._send_text(json.dumps(payload, separators=(",", ":")))

        deadline = time.monotonic() + self.timeout
        while time.monotonic() < deadline:
            message = self._recv_json()
            if message.get("id") != message_id:
                continue
            if "error" in message:
                error = message["error"]
                raise RuntimeError(f"{method} failed: {error}")
            return message.get("result", {})
        raise TimeoutError(f"Timed out waiting for {method}")

    def evaluate(self, expression: str, await_promise: bool = False) -> object:
        result = self.call(
            "Runtime.evaluate",
            {
                "expression": expression,
                "awaitPromise": await_promise,
                "returnByValue": True,
            },
        )
        remote = result.get("result", {})
        if "exceptionDetails" in result:
            raise RuntimeError(result["exceptionDetails"])
        return remote.get("value")

    def _open_socket(self, websocket_url: str) -> socket.socket:
        parsed = urllib.parse.urlparse(websocket_url)
        if parsed.scheme != "ws":
            raise ValueError(f"Only ws:// DevTools URLs are supported: {websocket_url}")

        port = parsed.port or 80
        path = urllib.parse.urlunparse(("", "", parsed.path or "/", "", parsed.query, ""))
        sock = socket.create_connection((parsed.hostname, port), timeout=self.timeout)
        sock.settimeout(self.timeout)

        key = base64.b64encode(os.urandom(16)).decode("ascii")
        request = (
            f"GET {path} HTTP/1.1\r\n"
            f"Host: {parsed.hostname}:{port}\r\n"
            f"Origin: http://127.0.0.1:{port}\r\n"
            "Upgrade: websocket\r\n"
            "Connection: Upgrade\r\n"
            f"Sec-WebSocket-Key: {key}\r\n"
            "Sec-WebSocket-Version: 13\r\n"
            "\r\n"
        )
        sock.sendall(request.encode("ascii"))
        response = self._read_http_headers(sock)
        if b" 101 " not in response.split(b"\r\n", 1)[0]:
            raise RuntimeError(f"DevTools WebSocket upgrade failed: {response!r}")
        return sock

    def _read_http_headers(self, sock: socket.socket) -> bytes:
        data = b""
        while b"\r\n\r\n" not in data:
            chunk = sock.recv(4096)
            if not chunk:
                break
            data += chunk
        headers, separator, rest = data.partition(b"\r\n\r\n")
        self.recv_buffer += rest
        return headers + separator

    def _send_text(self, text: str) -> None:
        payload = text.encode("utf-8")
        header = bytearray([0x81])
        length = len(payload)
        if length < 126:
            header.append(0x80 | length)
        elif length < 65536:
            header.extend([0x80 | 126])
            header.extend(struct.pack("!H", length))
        else:
            header.extend([0x80 | 127])
            header.extend(struct.pack("!Q", length))

        mask = os.urandom(4)
        masked = bytes(byte ^ mask[index % 4] for index, byte in enumerate(payload))
        self.sock.sendall(bytes(header) + mask + masked)

    def _recv_json(self) -> dict:
        while True:
            opcode, payload = self._recv_frame()
            if opcode == 0x8:
                raise RuntimeError("DevTools WebSocket closed")
            if opcode == 0x9:
                self._send_pong(payload)
                continue
            if opcode in (0x1, 0x2):
                return json.loads(payload.decode("utf-8"))

    def _recv_frame(self) -> tuple[int, bytes]:
        first = self._recv_exact(2)
        opcode = first[0] & 0x0F
        masked = bool(first[1] & 0x80)
        length = first[1] & 0x7F
        if length == 126:
            length = struct.unpack("!H", self._recv_exact(2))[0]
        elif length == 127:
            length = struct.unpack("!Q", self._recv_exact(8))[0]
        mask = self._recv_exact(4) if masked else b""
        payload = self._recv_exact(length)
        if masked:
            payload = bytes(byte ^ mask[index % 4] for index, byte in enumerate(payload))
        return opcode, payload

    def _recv_exact(self, count: int) -> bytes:
        chunks = []
        remaining = count
        if self.recv_buffer:
            chunk = self.recv_buffer[:remaining]
            self.recv_buffer = self.recv_buffer[remaining:]
            chunks.append(chunk)
            remaining -= len(chunk)
        while remaining:
            chunk = self.sock.recv(remaining)
            if not chunk:
                raise RuntimeError("Unexpected end of WebSocket stream")
            chunks.append(chunk)
            remaining -= len(chunk)
        return b"".join(chunks)

    def _send_pong(self, payload: bytes) -> None:
        header = bytearray([0x8A, 0x80 | len(payload)])
        mask = os.urandom(4)
        masked = bytes(byte ^ mask[index % 4] for index, byte in enumerate(payload))
        self.sock.sendall(bytes(header) + mask + masked)


def main() -> int:
    args = parse_args()
    html_path = args.html.resolve()
    output_path = args.output.resolve()
    if not html_path.exists():
        raise FileNotFoundError(html_path)
    if not output_path.parent.exists():
        raise FileNotFoundError(f"Output directory does not exist: {output_path.parent}")

    browser_path = find_browser(args.browser)
    with LocalServer(html_path.parent, args.port, html_path.name) as server:
        capture_page(
            browser_path=browser_path,
            url=server.url,
            output_path=output_path,
            width=args.width,
            height=args.height,
            timeout=args.timeout,
            image_wait=args.image_wait,
            settle_delay=args.settle_delay,
            block_external_fetches=args.block_external_fetches,
        )
    print(f"Saved {output_path} from {server.url}")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--html", type=Path, default=DEFAULT_HTML, help="HTML file to capture.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="PNG path to write.")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="Preferred local server port.")
    parser.add_argument("--width", type=int, default=DEFAULT_WIDTH, help="Viewport and image width.")
    parser.add_argument("--height", type=int, default=DEFAULT_HEIGHT, help="Viewport and image height.")
    parser.add_argument("--timeout", type=float, default=20, help="Browser automation timeout in seconds.")
    parser.add_argument(
        "--image-wait",
        type=float,
        default=8,
        help="Seconds to wait for page images before capturing. Use 0 to skip.",
    )
    parser.add_argument(
        "--settle-delay",
        type=float,
        default=DEFAULT_SETTLE_DELAY,
        help="Extra seconds to wait before capture so late image paints can finish.",
    )
    parser.add_argument(
        "--browser",
        type=Path,
        default=None,
        help="Path to msedge, chrome, chromium, or another Chromium-family browser.",
    )
    parser.add_argument(
        "--block-external-fetches",
        action="store_true",
        help="Disable page fetch() calls for deterministic offline fallback cards.",
    )
    return parser.parse_args()


def find_browser(explicit_path: Path | None) -> Path:
    if explicit_path:
        if explicit_path.exists():
            return explicit_path
        raise FileNotFoundError(explicit_path)

    env_path = os.environ.get("RANKER_BROWSER")
    if env_path and Path(env_path).exists():
        return Path(env_path)

    for name in ("msedge", "microsoft-edge", "google-chrome", "chrome", "chromium", "chromium-browser"):
        found = shutil.which(name)
        if found:
            return Path(found)

    candidates = []
    for root_var in ("ProgramFiles", "ProgramFiles(x86)", "LocalAppData"):
        root = os.environ.get(root_var)
        if not root:
            continue
        candidates.extend(
            [
                Path(root) / "Microsoft" / "Edge" / "Application" / "msedge.exe",
                Path(root) / "Google" / "Chrome" / "Application" / "chrome.exe",
            ]
        )
    for candidate in candidates:
        if candidate.exists():
            return candidate

    raise FileNotFoundError(
        "Could not find a Chromium-family browser. Pass --browser or set RANKER_BROWSER."
    )


def capture_page(
    browser_path: Path,
    url: str,
    output_path: Path,
    width: int,
    height: int,
    timeout: float,
    image_wait: float,
    settle_delay: float,
    block_external_fetches: bool,
) -> None:
    debug_port = find_free_port()
    with tempfile.TemporaryDirectory(prefix="ranker-og-browser-") as profile:
        process = subprocess.Popen(
            [
                str(browser_path),
                f"--remote-debugging-port={debug_port}",
                f"--user-data-dir={profile}",
                "--headless=new",
                "--no-sandbox",
                "--disable-gpu",
                "--disable-gpu-sandbox",
                "--disable-gpu-compositing",
                "--disable-dev-shm-usage",
                "--hide-scrollbars",
                "--no-first-run",
                "--disable-default-apps",
                "--no-default-browser-check",
                "--remote-allow-origins=*",
                "--disable-sync",
                "--use-angle=swiftshader",
                "--use-gl=swiftshader",
                "--window-position=0,0",
                f"--window-size={width},{height}",
                "about:blank",
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True,
        )
        try:
            websocket_url = open_blank_target(process, debug_port, timeout)
            with CdpConnection(websocket_url, timeout=timeout) as cdp:
                cdp.call("Page.enable")
                cdp.call("Runtime.enable")
                cdp.call(
                    "Emulation.setDeviceMetricsOverride",
                    {
                        "width": width,
                        "height": height,
                        "deviceScaleFactor": 1,
                        "mobile": False,
                    },
                )
                if block_external_fetches:
                    cdp.call(
                        "Page.addScriptToEvaluateOnNewDocument",
                        {"source": "window.fetch = async () => ({ ok: false, json: async () => ({}) });"},
                    )
                cdp.call("Page.navigate", {"url": url})
                wait_for_render(cdp, timeout)
                if image_wait > 0:
                    wait_for_images(cdp, image_wait)
                if settle_delay > 0:
                    time.sleep(settle_delay)
                cdp.evaluate(
                    "document.fonts && document.fonts.ready ? document.fonts.ready.then(() => true) : true",
                    await_promise=True,
                )
                screenshot = cdp.call(
                    "Page.captureScreenshot",
                    {
                        "format": "png",
                        "fromSurface": True,
                        "captureBeyondViewport": False,
                        "clip": {"x": 0, "y": 0, "width": width, "height": height, "scale": 1},
                    },
                )
        finally:
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=5)

    output_path.write_bytes(base64.b64decode(screenshot["data"]))


def open_blank_target(process: subprocess.Popen, debug_port: int, timeout: float) -> str:
    wait_for_debugger(process, debug_port, timeout)
    list_url = f"http://127.0.0.1:{debug_port}/json/list"
    with urllib.request.urlopen(list_url, timeout=timeout) as response:
        targets = json.loads(response.read().decode("utf-8"))
    for target in targets:
        if target.get("type") == "page" and target.get("webSocketDebuggerUrl"):
            return target["webSocketDebuggerUrl"]

    target_url = f"http://127.0.0.1:{debug_port}/json/new?about:blank"
    request = urllib.request.Request(target_url, method="PUT")
    with urllib.request.urlopen(request, timeout=timeout) as response:
        target = json.loads(response.read().decode("utf-8"))
    return target["webSocketDebuggerUrl"]


def wait_for_debugger(process: subprocess.Popen, debug_port: int, timeout: float) -> None:
    deadline = time.monotonic() + timeout
    version_url = f"http://127.0.0.1:{debug_port}/json/version"
    while time.monotonic() < deadline:
        if process.poll() is not None:
            _, stderr = process.communicate(timeout=1)
            raise RuntimeError(f"Browser exited before DevTools started.\n{stderr.strip()}")
        try:
            with urllib.request.urlopen(version_url, timeout=0.5) as response:
                if response.status == 200:
                    return
        except (OSError, urllib.error.URLError):
            time.sleep(0.1)
    raise TimeoutError("Browser DevTools endpoint did not start.")


def wait_for_render(cdp: CdpConnection, timeout: float) -> None:
    deadline = time.monotonic() + timeout
    expression = """
(() => ({
  readyState: document.readyState,
  cards: document.querySelectorAll(".taxon-card").length,
  title: document.querySelector("h1")?.textContent || ""
}))()
"""
    while time.monotonic() < deadline:
        state = cdp.evaluate(expression)
        if state and state["readyState"] in ("interactive", "complete") and state["cards"] > 0:
            return
        time.sleep(0.1)
    raise TimeoutError("Ranker page did not render cards before timeout.")


def wait_for_images(cdp: CdpConnection, timeout: float) -> None:
    deadline = time.monotonic() + timeout
    expression = """
(() => {
  const images = [...document.querySelectorAll("img[data-wiki-image]")];
  const sourced = images.filter((image) => image.currentSrc || image.src);
  return {
    total: images.length,
    hydrated: images.filter((image) => image.currentSrc || image.src || image.classList.contains("failed")).length,
    sourced: sourced.length,
    complete: sourced.filter((image) => image.complete).length
  };
})()
"""
    while time.monotonic() < deadline:
        state = cdp.evaluate(expression)
        if state and (
            state["total"] == 0
            or (state["hydrated"] >= state["total"] and state["complete"] >= state["sourced"])
        ):
            return
        time.sleep(0.25)


def find_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


if __name__ == "__main__":
    raise SystemExit(main())
