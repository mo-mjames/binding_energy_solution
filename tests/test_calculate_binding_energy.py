"""Unit tests for binding_energy_solution.calculate_binding_energy module"""

from binding_energy_solution.calculate_binding_energy import (
    calc_pair_binding_energy,
    calc_trio_binding_energy,
)


def test_calc_pair_binding_energy():
    """Test that function returns result for pair binding energy given by
    example in Technical Exercise"""
    r = 6.82e-10  # separation distance in m
    u = -1.0e-22  # binding energy in J
    assert calc_pair_binding_energy(r) == u


def test_calc_trio_binding_energy():
    """Test that function returns 3x the result for pair binding energy given
    by example in Technical Exercise"""
    r = 6.82e-10  # separation distance in m
    u = -1.0e-22  # binding energy in J
    assert calc_trio_binding_energy(r, r, r) == 3 * u
