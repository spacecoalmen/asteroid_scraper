import argparse
from numpy.core.umath import deg2rad
import pandas
from asteroid_scraper.finder import AsteroidFinder
from asteroid_scraper.utils.dataframe_normalizer import normalize_asteroids


def main():
    parser = argparse.ArgumentParser(
        description="Find asteroids that can be mined by the cycler"
    )

    parser.add_argument('asteroids',
                        help='asteroids orbits csv file obtained at '
                             'http://ssd.jpl.nasa.gov/sbdb_query.cgi')
    parser.add_argument('cycler',
                        help='cycler orbits csv file')

    parser.add_argument('-o', '--output',
                        default='example_files/results/results.csv',
                        help='output file path',
                        type=str)

    parser.add_argument('-l', '--limit',
                        default=100,
                        help='limit the top N matches',
                        type=int)

    parser.add_argument('-a', '--min_semiax',
                        default=1.0,
                        help='asteroid minimun semiax',
                        type=float)
    parser.add_argument('-A', '--max_semiax',
                        default=1.7,
                        help='asteroid maximum semiax',
                        type=float)

    parser.add_argument('-e', '--min_ecce',
                        default=0.0,
                        help='asteroid minimum orbital eccentricity',
                        type=float)
    parser.add_argument('-E', '--max_ecce',
                        default=0.45,
                        help='asteroid maximum orbital eccentricity',
                        type=float)

    parser.add_argument('-i', '--min_incl',
                        default=0.0,
                        help='asteroid minimum incl (rad)',
                        type=float)
    parser.add_argument('-I', '--max_incl',
                        default=0.35,
                        help='asteroid maximum incl (rad)',
                        type=float)

    opts = parser.parse_args()

    with open(opts.cycler, 'r') as _file:
        cycler_orbits_df = pandas.read_csv(_file, header=0)

    with open(opts.asteroids, 'r') as _file:
        asteroids_orbits_df = pandas.read_csv(_file, header=0)
        normalize_asteroids(asteroids_orbits_df)

    finder = AsteroidFinder(opts.min_semiax,
                            opts.max_semiax,
                            opts.min_ecce,
                            opts.max_ecce,
                            opts.min_incl,
                            opts.max_incl)
    tisserand_criterion_results, q_function_result = finder.find_asteroids(cycler_orbits_df,
                                                                           asteroids_orbits_df)

    tisserand_criterion_results.head(opts.limit).to_csv('results/tisserand_criterion_result.csv')
    q_function_result.head(opts.limit).to_csv(opts.output)
