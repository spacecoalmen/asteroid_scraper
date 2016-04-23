import random


def find_asteroids(cycler_orbits, asteroid_orbits):
    """
    return asteroid orbits that meet the cycler orbit requirements
    """

    result = []
    for cycler_orbit in cycler_orbits:
        for asteroid_orbit in asteroid_orbits:
            if dummy_function():
                result.append(asteroid_orbit)

    return result


def dummy_function():
    return bool(random.getrandbits(1))
