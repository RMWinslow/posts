# Heightmap Erosion Lab

Open [index.html](C:\Users\rober\git\posts\maps\erosion\index.html) in a browser to run a local WebGL port of the erosion shader.

What it does:

- Replaces the ShaderToy mouse-painted Buffer A with a grayscale heightmap image.
- Derives height and slope from the input image in a preprocessing pass.
- Runs the original erosion filter logic as a second GPU pass.
- Previews shaded relief, eroded height, erosion delta, ridge map, and debug output.
- Exports the eroded heightmap as a grayscale PNG.

Notes:

- White pixels are interpreted as high terrain and black pixels as low terrain.
- If your browser blocks local image loading from `file://`, run a simple local server in this folder and open `index.html` through `http://localhost/...`.
- The local port keeps the core erosion math from `shadertoy_buffer_b.glsl` but omits the full ShaderToy keyboard toggles and 3D terrain raymarcher.
