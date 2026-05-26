# Erosion Filter Scratchpad

## Attribution

The erosion technique used here is the **Advanced Terrain Erosion Filter** by
**Rune Skovbo Johansen**, copyright (c) 2025. The Phacelle Noise function used
by the erosion filter is also by Rune Skovbo Johansen, copyright (c) 2025.

Both are licensed under the **Mozilla Public License, v. 2.0**.
Full license text: https://mozilla.org/MPL/2.0/

- **Shader**: https://www.shadertoy.com/view/sf23W1
- **Blog post**: https://blog.runevision.com/2026/03/fast-and-gorgeous-erosion-filter.html

The technique was originally derived from versions by
[Clay John](https://www.shadertoy.com/view/MtGcWh) and
[Fewes](https://www.shadertoy.com/view/7ljcRW).
The terrain rendering in the Image buffer is also derived from Fewes' ShaderToy.

The `shadertoy_*.glsl` files in this folder contain the original shader source
code copied from [the ShaderToy page](https://www.shadertoy.com/view/sf23W1) for reference.



## Data Structures

buffer_a creates a vec3 structure:
    This maps points p -> data xyz (with interpolation in point p isn't exactly present)
    x is height, normalized to a 0-1 scale
    y and z are the directional derivatives of the height
    So together that are height and slope.
    The code in shader_a applies a brush to edit this 3 vector in a way that keeps height and slope consistent.
    x (height) is normalized to [0,1],
    and the underlying position space p is a 2d space spanning [0,1] in each direction.
    So a slope of one would take use from the bottom of the height range to the top across the width of the image.

buffer_b has heightmap function and an erosion filter function

heightmap takes a normalized position p:
    grabs the n=(height, x_gradient, y_gradient) from buffer a
    passes in p and n into the erosion filter,
    uses the results to compute a simple tree simulation,
    then packs them up using some language specific data structure weirdness


phacelle is a vec 4 corresponding to sine wave cells we generated
    x is the magnitude of the phase cell noise
    y is the derivative of that
    z and w are a direction vector for the stripe 
    yzw combine into a gradient in the usual 2d space


## Implementation References

Leveller is worth keeping in mind as a reference implementation. Its resource
page links C++ source for an Erode/Phacelle plugin based on Rune's shader.
Checked 2026-05-25: the public source zip contains only the Phacelle/Erosion
kernel plus a small GLSL type shim. The exported function has the signature
`ErosionFilter(settings, p, heightAndSlope, fadeTarget)`, so the plugin source
expects `heightAndSlope.yz` to already contain slope; it does not show how
Leveller computes slope from the underlying heightfield.

What remains unknown is Leveller's application-side slope convention. Public
Leveller pages mention slope maps, curvature maps, normal maps, and a slope
evaluation kernel, which suggests this lives in broader app/render/cache code,
not in the published Phacelle kernel. For this standalone PNG-in/PNG-out port,
the slope derivation is still our own compatibility choice rather than
something copied directly from Leveller.


## WebGL Proof of Concept

`phacelle_web_poc.html` is a single-file, self-contained WebGL2 prototype:
no server, no Node, no packages, and no external scripts. It generates a
512x512 normalized `p` texture, a 512x512 radial `normDir` texture pointing
away from the center, runs one Phacelle noise pass in a fragment shader, and
displays the RGBA result plus each output channel as grayscale. The input
textures are also displayed directly, which makes it easy to confirm that the
position gradient and direction wheel are correct before debugging Phacelle.

For the visualized output, Phacelle returns `(cosWave, sinWave, sideDir.x,
sideDir.y)`. When displaying this as RGBA, all four channels need to be encoded
into `[0, 1]`; forcing alpha to 1 hides `sideDir.y` and makes the fourth
grayscale debug view useless.

The current POC uses `RGBA8` textures for the generated input buffers because
that path is simple to display with 2D canvas. That should not be treated as
the final data model. In WebGL2, uploading and sampling 32-bit float textures
from `Float32Array` is standard. Rendering into 16-bit or 32-bit float textures
requires `EXT_color_buffer_float`, but current browser support is broad enough
that the real pipeline should probably feature-detect it and prefer `RG32F` or
`RGBA32F` for clarity, with `RG16F`/`RGBA16F` or packed formats only as fallback
or memory-saving options. At large sizes, memory bandwidth is likely a bigger
constraint than basic browser support.
