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

## Local Port

`index.html` is a local WebGL port that swaps out the ShaderToy mouse-painted
Buffer A workflow for a grayscale image input. It preprocesses the source image
into height plus slope data, then runs the erosion filter locally and previews
the result in 2D.
