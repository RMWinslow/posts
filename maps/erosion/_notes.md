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
