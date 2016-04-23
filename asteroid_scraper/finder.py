from numpy import NaN
from numpy.core.umath import deg2rad
from pandas import DataFrame
from asteroid_scraper.math.qfunction import Qfunction
from asteroid_scraper.math.tisserand import tisserand

MIN_SEMIAX = 1
MAX_SEMIAX = 1.7
MIN_ECCE = 0
MAX_ECCE = 0.45
MIN_INCL = 0
MAX_INCL = deg2rad(20)


def find_asteroids(cycler_orbits, asteroids_orbits):
    """
    return asteroid orbits that meet the filter requirement, each asteroid have tisserand value and
    tisserand delta with the cycler orbit
    """


    asteroids_orbits['tisserand'] = asteroids_orbits.apply(lambda row: tisserand(row), axis=1)
    asteroids_orbits['q_function'] = asteroids_orbits.apply(lambda row: Qfunction(row), axis=1)
    cycler_orbits['tisserand'] = cycler_orbits.apply(lambda row: tisserand(row), axis=1)
    cycler_orbits['q_function'] = cycler_orbits.apply(lambda row: Qfunction(row), axis=1)

    # from now, we treat data as dict data structure instead of pandas data frame, need more exp ;)

    cycler_orbits = cycler_orbits.to_dict(orient="records")
    asteroids_orbits = asteroids_orbits.to_dict(orient="records")

    asteroids_orbits = filter_asteroids(asteroids_orbits)

    tisserand_criterion_results = []
    q_function_result = []

    for i, cycler_orbit in enumerate(cycler_orbits):
        for orbit in asteroids_orbits:
            delta_tisserand = _tisserand_delta(cycler_orbit['tisserand'], orbit['tisserand'])
            delta_q_function = _q_function_delta(cycler_orbit['q_function'], orbit['q_function'])

            tisserand_criterion_results.append({'delta_tisserand': delta_tisserand,
                                                'asteroid_id': orbit['id'],
                                                'asteroid_full_name': orbit['full_name'],
                                                'asteroid_tisserand': orbit['tisserand'],
                                                'cycler_orbit_tisserand': cycler_orbit['tisserand'],
                                                'cycler_orbit_index': i
                                                })
            q_function_result.append({'delta_q_function': delta_q_function,
                                      'asteroid_id': orbit['id'],
                                      'asteroid_full_name': orbit['full_name'],
                                      'asteroid_q_function': orbit['q_function'],
                                      'cycler_orbit_q_function': cycler_orbit['q_function'],
                                      'cycler_orbit_index': i
                                      })

    # back to pandas data frame data structure
    tisserand_criterion_results = DataFrame(tisserand_criterion_results)
    tisserand_criterion_results = tisserand_criterion_results.sort_values('delta_tisserand')

    q_function_result = DataFrame(q_function_result)
    q_function_result = q_function_result.sort_values('delta_q_function', ascending=True)
    return tisserand_criterion_results, q_function_result


def filter_asteroids(asteroids_orbits):
    results = []
    for orbit in asteroids_orbits:
        if MIN_SEMIAX <= orbit['semiax'] <= MAX_SEMIAX \
            and MIN_ECCE <= orbit['ecce'] <= MAX_ECCE \
                and MIN_INCL <= orbit['incl'] <= MAX_INCL:
                    results.append(orbit)

    return results


def _tisserand_delta(t1, t2):
    try:
        return abs(t1 - t2)
    except TypeError:
        print 'error on tisserand_delta', t1, t2
        return NaN


def _q_function_delta(t1, t2):
    try:
        return abs(t1 - t2)
    except TypeError:
        print 'error on _q_function_delta', t1, t2
        return NaN
