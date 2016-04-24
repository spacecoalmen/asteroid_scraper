import argparse
import logging
import pprint
import pandas
import sys
from asteroid_scraper.finder import AsteroidFinder
from asteroid_scraper.utils.dataframe_normalizer import normalize_asteroids


def main():
    parser = argparse.ArgumentParser(
        description="Find asteroids eligible to be mined by the cycler"
    )

    parser.add_argument('cycler',
                        help='cycler orbits .csv file')
    parser.add_argument('asteroids',
                        help='asteroids orbits .csv file obtained at '
                             'http://ssd.jpl.nasa.gov/sbdb_query.cgi')

    parser.add_argument('-o', '--output',
                        default='example_files/results/results.csv',
                        help='output .csv file path',
                        type=str)

    parser.add_argument('-l', '--limit',
                        default=100,
                        help='limit the top N matches',
                        type=int)
    parser.add_argument('-s', '--sort_key',
                        choices=['tisserand', 'q_function'],
                        default='tisserand',
                        help='sort by tisserand delta or q_function delta',
                        type=str)

    parser.add_argument('-a', '--min_semiaxis',
                        default=1.0,
                        help='asteroid minimum semi major axis ',
                        type=float)
    parser.add_argument('-A', '--max_semiaxis',
                        default=1.7,
                        help='asteroid maximum semi major axis',
                        type=float)

    parser.add_argument('-e', '--min_eccentricity',
                        default=0.0,
                        help='asteroid minimum orbital eccentricity',
                        type=float)
    parser.add_argument('-E', '--max_eccentricity',
                        default=0.45,
                        help='asteroid maximum orbital eccentricity',
                        type=float)

    parser.add_argument('-i', '--min_inclination',
                        default=0.0,
                        help='asteroid minimum inclination to ecliptic (rad)',
                        type=float)
    parser.add_argument('-I', '--max_inclination',
                        default=0.35,
                        help='asteroid maximum inclination to ecliptic (rad)',
                        type=float)

    opts = parser.parse_args()

    with open(opts.cycler, 'r') as _file:
        cycler_orbits_df = pandas.read_csv(_file, header=0)

    with open(opts.asteroids, 'r') as _file:
        asteroids_orbits_df = pandas.read_csv(_file, header=0)
        asteroids_orbits_df = normalize_asteroids(asteroids_orbits_df)

    finder = AsteroidFinder(opts.min_semiaxis,
                            opts.max_semiaxis,
                            opts.min_eccentricity,
                            opts.max_eccentricity,
                            opts.min_inclination,
                            opts.max_inclination,
                            opts.sort_key)
    results = finder.find_asteroids(cycler_orbits_df, asteroids_orbits_df)

    asteroids_found = len(results['asteroid_id'].value_counts())
    asteroids_total = len(asteroids_orbits_df['id'].value_counts())

    pprint.pprint("Found %s asteroids on a total of %s"
                  % (asteroids_found, asteroids_total))
    results[:opts.limit].to_csv(opts.output)
    pprint.pprint("Scraping done, results are in %s" % opts.output)
