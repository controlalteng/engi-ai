import numpy as np

def mean(xs):
    return float(np.mean(xs)) if len(xs) else float("nan")
