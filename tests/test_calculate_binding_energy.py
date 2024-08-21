import pytest
import binding_energy_solution.calculate_binding_energy as calculate_binding_energy


def test_calc_pair_binding_energy():
    """Test that function returns result for pair binding energy given by example in Technical Exercise"""
    r = 6.82e-10  # separation distance in m
    u = -1.0e-22  # binding energy in J
    assert calculate_binding_energy.calc_pair_binding_energy(r) == u
