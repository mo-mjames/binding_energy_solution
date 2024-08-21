
def calc_pair_binding_energy(separation_distance):
    """
    Calculate the binding energy of a pair of particles separated by a given distance.

    Parameters
    ----------
    separation_distance : float
        The distance between two particles in metres.

    Returns
    -------
    float
        The binding energy of the pair of particles in joules.
    """

    # Constants
    epsilon = 1.65e-21  # J
    sigma = 3.41e-10  # m

    # Calculate the binding energy
    pair_binding_energy = (
        4
        * epsilon
        * ((sigma / separation_distance) ** 12 - (sigma / separation_distance) ** 6)
    )

    return pair_binding_energy
