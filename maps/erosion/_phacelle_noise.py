"""Direct Python port of the ShaderToy Phacelle Noise helper.

This file intentionally keeps the original GLSL naming around PhacelleNoise so
the Python version can be cross-referenced against shadertoy_buffer_b.glsl.
"""

from __future__ import annotations

from math import cos, exp, floor, sin, sqrt

from numpy import dot


# NOTE: Phacelle Noise depends on the 'hash' function defined in the Common tab.

TAU = 6.28318530717959
Vec2 = tuple[float, float]
Vec4 = tuple[float, float, float, float]


def fract(p: Vec2) -> Vec2:
    """GLSL fract(vec2): return the fractional part of each component."""
    return p[0] - floor(p[0]), p[1] - floor(p[1])


def hash(x: Vec2) -> Vec2:
    """Port of hash(vec2 x) from shadertoy_common.glsl."""
    k = (0.3183099, 0.3678794)
    x = x[0] * k[0] + k[1], x[1] * k[1] + k[0]
    inner = x[0] * x[1] * (x[0] + x[1])
    inner = inner - floor(inner)
    f = fract((16.0 * k[0] * inner, 16.0 * k[1] * inner))
    return -1.0 + 2.0 * f[0], -1.0 + 2.0 * f[1]




# The Simple Phacelle Noise function produces a stripe pattern aligned with the input vector.
# The name Phacelle is a portmanteau of phase and cell, since the function produces a phase by
# interpolating cosine and sine waves from multiple cells.
#  - p is the input point being evaluated.
#  - normDir is the direction of the stripes at this point. It must be a normalized vector.
#  - freq is the freqency of the stripes within each cell. It's best to keep it close to 1.0, as
#    high values will produce distortions and other artifacts.
#  - offset is the phase offset of the stripes, where 1.0 is a full cycle.
#  - normalization is the degree of normalization applied, between 0 and 1. With e.g. a value of
#    0.4, raw output with a magnitude below 0.6 won't get fully normalized to a magnitude of 1.0.
# Phacelle Noise function copyright (c) 2025 Rune Skovbo Johansen
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
def PhacelleNoise(
    p: Vec2, #MYNOTE: actaully p*freq
    normDir: Vec2,
    freq: float, #MYNOTE: actaully cellScale
    offset: float,
    normalization: float,
) -> Vec4:
    # Get a vector orthogonal to the input direction, with a
    # magnitude proportional to the frequency of the stripes.
    sideDir = -normDir[1] * freq * TAU, normDir[0] * freq * TAU
    offset *= TAU

    # Iterate over 4x4 cells, calculating a stripe pattern for each and blending between them.
    # pInt is the integer part of the current coordinate p, pFrac is the remainder.
    #
    # o   o   o   o
    #
    # o   o   o   o
    #       p
    # o   i   o   o
    #
    # o   o   o   o
    #
    # p: current coordinate    i: integer part of p    o: grid points for 4x4 cells
    #
    pInt = floor(p[0]), floor(p[1])
    pFrac = fract(p)
    phaseDir = 0.0, 0.0
    weightSum = 0.0
    for i in range(-1, 3):
        for j in range(-1, 3):
            gridOffset = float(i), float(j)

            # Calculate a cell point by starting off with a point in the integer grid.
            gridPoint = pInt[0] + gridOffset[0], pInt[1] + gridOffset[1]

            # Calculate a random offset for the cell point between -0.5 and 0.5 on each axis.
            randomOffset = hash(gridPoint)
            randomOffset = randomOffset[0] * 0.5, randomOffset[1] * 0.5

            # The final cell point (we don't store it) is the gridPoint plus the randomOffset.
            # Calculate a vector representing the input point relative to this cell point:
            # p - (gridPoint + randomOffset)
            # = (pFrac + pInt) - ((pInt + gridOffset) + randomOffset)
            # = pFrac + pInt - pInt - gridOffset - randomOffset
            # = pFrac - gridOffset - randomOffset
            vectorFromCellPoint = (
                pFrac[0] - gridOffset[0] - randomOffset[0],
                pFrac[1] - gridOffset[1] - randomOffset[1],
            )

            # Bell-shaped weight function which is 1 at dist 0 and nearly 0 at dist 1.5.
            # Due to the random offsets of up to 0.5, the closest a cell point not in the 4x4
            # grid can be to the current point p is 1.5 units away.
            sqrDist = dot(vectorFromCellPoint, vectorFromCellPoint)
            weight = exp(-sqrDist * 2.0)
            # Subtract 0.01111 to make the function actually 0 at distance 1.5, which avoids
            # some (very subtle) grid line artefacts.
            weight = max(0.0, weight - 0.01111)

            # Keep track of the total sum of weights.
            weightSum += weight

            # The waveInput is a gradient which increases in value along sideDir. Its rate of
            # change is the freq times tau, due to the multiplier pre-applied to sideDir.
            waveInput = dot(vectorFromCellPoint, sideDir) + offset

            # Add this cell's cosine and sine wave contributions to the interpolated value.
            phaseDir = (
                phaseDir[0] + cos(waveInput) * weight,
                phaseDir[1] + sin(waveInput) * weight,
            )

    # Get the raw interpolated value.
    interpolated = phaseDir[0] / weightSum, phaseDir[1] / weightSum
    # Interpret the value as a vector whose length represents the magnitude of both waves.
    magnitude = sqrt(dot(interpolated, interpolated))
    # Apply a lower threshold to show small magnitudes we're going to fully normalize.
    magnitude = max(1.0 - normalization, magnitude)
    # Return a vector containing the normalized cosine and sine waves, as well as the direction
    # vector, which can be multiplied onto the sine to get the derivatives of the cosine.
    return interpolated[0] / magnitude, interpolated[1] / magnitude, sideDir[0], sideDir[1]
