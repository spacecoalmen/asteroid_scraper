from numpy import NaN
from numpy.core.umath import deg2rad
from pandas import DataFrame
from asteroid_scraper.math.qfunction import Qfunction
from asteroid_scraper.math.tisserand import tisserand
from asteroid_scraper.utils.progress_bar import ProgressBarThread


class AsteroidFinder(object):
    __shared_state = {}
    client = None

    def _borg_init(self, min_semiax, max_semiax, min_ecce, max_ecce, min_incl, max_incl, sort_key):
        self.min_semiax = min_semiax
        self.max_semiax = max_semiax
        self.min_ecce = min_ecce
        self.max_ecce = max_ecce
        self.min_incl = min_incl
        self.max_incl = max_incl
        self.sort_key = sort_key

    def __init__(self, min_semiax, max_semiax, min_ecce, max_ecce, min_incl, max_incl, sort_key):
        self.__dict__ = self.__shared_state
        if not self.__shared_state:
            self._borg_init(min_semiax, max_semiax, min_ecce, max_ecce, min_incl, max_incl, sort_key)

    def find_asteroids(self, cycler_orbits, asteroids_orbits):
        """
        return asteroid orbits that meet the filter requirement, each asteroid have tisserand value and
        tisserand delta with the cycler orbit
        """
        progress_bar = ProgressBarThread()
        progress_bar.start()

        asteroids_orbits['tisserand'] = asteroids_orbits.apply(lambda row: tisserand(row), axis=1)
        asteroids_orbits['q_function'] = asteroids_orbits.apply(lambda row: Qfunction(row), axis=1)
        cycler_orbits['tisserand'] = cycler_orbits.apply(lambda row: tisserand(row), axis=1)
        cycler_orbits['q_function'] = cycler_orbits.apply(lambda row: Qfunction(row), axis=1)

        # from now, we treat data as dict data structure instead of pandas data frame,
        # need more expertise with pandas API ;)

        cycler_orbits = cycler_orbits.to_dict(orient="records")
        asteroids_orbits = asteroids_orbits.to_dict(orient="records")

        asteroids_orbits = self.filter_asteroids(asteroids_orbits)

        results = []

        for i, cycler_orbit in enumerate(cycler_orbits):

            cycler_tisserand = cycler_orbit['tisserand']
            cycler_q_function = cycler_orbit['q_function']
            for orbit in asteroids_orbits:

                delta_tisserand = self._tisserand_delta(cycler_tisserand,
                                                        orbit['tisserand'])
                delta_q_function = self._q_function_delta(cycler_q_function,
                                                          orbit['q_function'])

                results.append({'asteroid_id': orbit['id'],
                                'asteroid_full_name': orbit['full_name'],
                                'asteroid_tisserand': orbit['tisserand'],
                                'asteroid_q_function': orbit['q_function'],
                                'cycler_orbit_index': i,
                                'cycler_orbit_tisserand': cycler_tisserand,
                                'cycler_orbit_q_function': cycler_q_function,
                                'delta_q_function': delta_q_function,
                                'delta_tisserand': delta_tisserand,
                                })

        # back to pandas data frame data structure
        results = DataFrame(results)
        results = results.sort_values('delta_'+self.sort_key)
        progress_bar.stop()
        return results

    def filter_asteroids(self, asteroids_orbits):
        results = []
        # should be filtered using pandas API in order to achieve efficency
        for orbit in asteroids_orbits:
            if self.min_semiax <= orbit['semiax'] <= self.max_semiax \
                and self.min_ecce <= orbit['ecce'] <= self.max_ecce \
                    and self.min_incl <= orbit['incl'] <= self.max_incl:
                        results.append(orbit)

        return results

    def _tisserand_delta(self, t1, t2):
        try:
            return abs(t1 - t2)
        except TypeError:
            print 'error on tisserand_delta', t1, t2
            return NaN

    def _q_function_delta(self, t1, t2):
        try:
            return abs(t1 - t2)
        except TypeError:
            print 'error on q_function_delta', t1, t2
            return NaN
