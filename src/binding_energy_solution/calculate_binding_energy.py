"""
Module containing functions to calculate the binding energy of a pair or trio
of particles.
"""

from binding_energy_solution.constants import EPSILON, SIGMA, SEP_1_2, SEP_1_3, SEP_2_3


def calc_pair_binding_energy(epsilon, sigma, separation_distance):
    """
    Calculate the binding energy of a pair of particles separated by a given
    distance.

    Parameters
    ----------
    separation_distance : float
        The distance between two particles in metres.

    Returns
    -------
    float
        The binding energy of the pair of particles in joules.
    """

    # Calculate the binding energy
    pair_binding_energy = (
        4
        * epsilon
        * ((sigma / separation_distance) ** 12 - (sigma / separation_distance) ** 6)
    )

    return pair_binding_energy


def calc_trio_binding_energy(
    epsilon, sigma, separation_1_2, separation_1_3, separation_2_3
):
    """
    Calculate the binding energy of a trio of particles separated by given
    distances.

    Parameters
    ----------
    separation_1_2 : float
        The distance between particles 1 and 2 in metres.
    separation_1_3 : float
        The distance between particles 1 and 3 in metres.
    separation_2_3 : float
        The distance between particles 2 and 3 in metres.

    Returns
    -------
    float
        The binding energy of the trio of particles in joules.
    """

    binding_energy_1_2 = calc_pair_binding_energy(epsilon, sigma, separation_1_2)
    binding_energy_1_3 = calc_pair_binding_energy(epsilon, sigma, separation_1_3)
    binding_energy_2_3 = calc_pair_binding_energy(epsilon, sigma, separation_2_3)
    trio_binding_energy = binding_energy_1_2 + binding_energy_1_3 + binding_energy_2_3
    return trio_binding_energy


def main():
    """main funtion to call functions"""
    result_trio_binding_energy = calc_trio_binding_energy(
        epsilon=EPSILON,
        sigma=SIGMA,
        separation_1_2=SEP_1_2,
        separation_1_3=SEP_1_3,
        separation_2_3=SEP_2_3,
    )
    print(result_trio_binding_energy)


if __name__ == "__main__":
    main()
