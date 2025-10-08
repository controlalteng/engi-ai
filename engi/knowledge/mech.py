def stress(force_n: float, area_mm2: float) -> float:
  """σ = F/A (MPa). F em N, A em mm²."""
  return (force_n / area_mm2) / 1e6
