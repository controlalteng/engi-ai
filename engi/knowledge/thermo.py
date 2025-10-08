def efficiency(th_k: float, tc_k: float) -> float:
    """Carnot: η = 1 - Tc/Th (Th, Tc em Kelvin)."""
    return 1.0 - (tc_k / th_k)
