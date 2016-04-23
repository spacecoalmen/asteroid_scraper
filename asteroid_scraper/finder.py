import random
from asteroid_scraper.math import tisserand


def find_asteroids(cycler_orbits, asteroids):
    """
    return asteroid orbits that meet the cycler orbit requirements
    """

    results = []
    asteroids = filter_asteroids(asteroids)

    for cycler_orbit in cycler_orbits:
        cycler_orbit['tisserand'] = tisserand.tisserand(tisserand.earth, cycler_orbit)
        for asteroid in asteroids:
            asteroid['tisserand'] = tisserand.tisserand(tisserand.earth, asteroid)
            tisserand_delta = abs(cycler_orbit['tisserand']-asteroid['tisserand'])
            results.append({'asteroid': asteroid,
                            'cycler_orbit': cycler_orbit,
                            'tisserand_delta': tisserand_delta
                            })
    print results
    return results


def filter_asteroids(asteroids):
    results = []
    for asteroid in asteroids:
        if asteroid['semiax'] >= 1 and asteroid['semiax'] <= 1.7:
            if asteroid['ecce'] >= 0 and asteroid['ecce'] <= 0.45:
                if asteroid['incl'] >= 0 and asteroid['incl'] <= 20:
                    results.append(asteroid)

    return results
