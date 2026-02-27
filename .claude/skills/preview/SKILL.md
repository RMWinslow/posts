---
name: preview
description: Preview an HTML file in Edge via a local HTTP server. Use when the user wants to view or test an HTML page locally.
disable-model-invocation: true
argument-hint: [path/to/file.html]
---

Preview a local HTML file in Edge using a temporary Python HTTP server.
This avoids CORS issues that occur when opening HTML files directly via file://.

## Steps

1. Determine the file to preview:
   - If `$ARGUMENTS` is provided, use that as the file path (relative to the repo root).
   - If no argument, ask the user which HTML file to preview.

2. Start a Python HTTP server in the background on port 8000 from the repo root:
   ```
   python -m http.server 8000
   ```
   Run this in the background using `run_in_background: true`.

3. Open the file in Edge:
   ```
   "/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe" "http://localhost:8000/<path>"
   ```

4. Tell the user the page is open and ask them to let you know when they're done previewing.

5. When the user says they're done, stop the background HTTP server using TaskStop with the task ID from step 2.

6. Confirm the server has been shut down.

## Important notes
- The server runs from the repo root so all relative paths within the HTML will work.
- Port 8000 is used by default. If it's already in use, try 8001, 8002, etc.
- Do NOT leave the server running after the user is done.
