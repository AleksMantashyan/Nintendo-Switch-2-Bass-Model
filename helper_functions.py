import numpy as np


def bass_cumulative(t, p, q, M):
    """Cumulative Bass diffusion curve."""
    t = np.asarray(t, dtype=float)
    e = np.exp(-(p + q) * t)
    return M * (1 - e) / (1 + (q / p) * e)
