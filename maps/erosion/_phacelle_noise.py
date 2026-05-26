"""Direct Python port of the ShaderToy Phacelle Noise helper.

This file intentionally keeps the original GLSL naming around PhacelleNoise so
the Python version can be cross-referenced against shadertoy_buffer_b.glsl.
"""

from __future__ import annotations

import numpy as np


# NOTE: Phacelle Noise depends on the 'hash' function defined in the Common tab.

TAU = 6.28318530717959


def fract(x: np.ndarray | float) -> np.ndarray:
    """GLSL fract(x): return the fractional part of x."""
    x = np.asarray(x, dtype=np.float64)
    return x - np.floor(x)


def hash(x: np.ndarray) -> np.ndarray:
    """Port of hash(vec2 x) from shadertoy_common.glsl."""
    k = np.array([0.3183099, 0.3678794], dtype=np.float64)
    x = np.asarray(x, dtype=np.float64)
    x = x * k + k[::-1]
    inner = fract(x[..., 0] * x[..., 1] * (x[..., 0] + x[..., 1]))
    return -1.0 + 2.0 * fract(16.0 * k * np.expand_dims(inner, axis=-1))


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
    p: np.ndarray,
    normDir: np.ndarray,
    freq: float,
    offset: float,
    normalization: float,
) -> np.ndarray:
    # Get a vector orthogonal to the input direction, with a
    # magnitude proportional to the frequency of the stripes.
    p = np.asarray(p, dtype=np.float64)
    normDir = np.asarray(normDir, dtype=np.float64)
    sideDir = normDir[..., ::-1] * np.array([-1.0, 1.0], dtype=np.float64) * freq * TAU
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
    pInt = np.floor(p)
    pFrac = fract(p)
    phaseDir = np.zeros_like(p, dtype=np.float64)
    weightSum = np.zeros(p.shape[:-1], dtype=np.float64)
    for i in range(-1, 3):
        for j in range(-1, 3):
            gridOffset = np.array([i, j], dtype=np.float64)

            # Calculate a cell point by starting off with a point in the integer grid.
            gridPoint = pInt + gridOffset

            # Calculate a random offset for the cell point between -0.5 and 0.5 on each axis.
            randomOffset = hash(gridPoint) * 0.5

            # The final cell point (we don't store it) is the gridPoint plus the randomOffset.
            # Calculate a vector representing the input point relative to this cell point:
            # p - (gridPoint + randomOffset)
            # = (pFrac + pInt) - ((pInt + gridOffset) + randomOffset)
            # = pFrac + pInt - pInt - gridOffset - randomOffset
            # = pFrac - gridOffset - randomOffset
            vectorFromCellPoint = pFrac - gridOffset - randomOffset

            # Bell-shaped weight function which is 1 at dist 0 and nearly 0 at dist 1.5.
            # Due to the random offsets of up to 0.5, the closest a cell point not in the 4x4
            # grid can be to the current point p is 1.5 units away.
            sqrDist = np.sum(vectorFromCellPoint * vectorFromCellPoint, axis=-1)
            weight = np.exp(-sqrDist * 2.0)
            # Subtract 0.01111 to make the function actually 0 at distance 1.5, which avoids
            # some (very subtle) grid line artefacts.
            weight = np.maximum(0.0, weight - 0.01111)

            # Keep track of the total sum of weights.
            weightSum += weight

            # The waveInput is a gradient which increases in value along sideDir. Its rate of
            # change is the freq times tau, due to the multiplier pre-applied to sideDir.
            waveInput = np.sum(vectorFromCellPoint * sideDir, axis=-1) + offset

            # Add this cell's cosine and sine wave contributions to the interpolated value.
            phaseDir += np.stack((np.cos(waveInput), np.sin(waveInput)), axis=-1) * np.expand_dims(
                weight, axis=-1
            )

    # Get the raw interpolated value.
    interpolated = phaseDir / np.expand_dims(weightSum, axis=-1)
    # Interpret the value as a vector whose length represents the magnitude of both waves.
    magnitude = np.sqrt(np.sum(interpolated * interpolated, axis=-1))
    # Apply a lower threshold to show small magnitudes we're going to fully normalize.
    magnitude = np.maximum(1.0 - normalization, magnitude)
    # Return a vector containing the normalized cosine and sine waves, as well as the direction
    # vector, which can be multiplied onto the sine to get the derivatives of the cosine.
    return np.concatenate((interpolated / np.expand_dims(magnitude, axis=-1), sideDir), axis=-1)
