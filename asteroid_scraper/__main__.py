import argparse
import pprint
import pandas
from asteroid_scraper.finder import find_asteroids
from asteroid_scraper.math.tisserand import tisserand
from asteroid_scraper.utils.dataframe_normalizer import normalize_asteroids


def main():

    parser = argparse.ArgumentParser(
        description="Find asteroids that can be mined by the cycler"
    )

    parser.add_argument('-m', '--asteroid_file',
                        help='asteroid orbits csv file')
    parser.add_argument('-c', '--cycler_file',
                        help='cycler orbits csv file')

    opts = parser.parse_args()

    with open(opts.cycler_file, 'r') as _file:
        cycler_orbits_df = pandas.read_csv(_file, header=0)

    with open(opts.asteroid_file, 'r') as _file:
        asteroids_orbits_df = pandas.read_csv(_file, header=0)
        normalize_asteroids(asteroids_orbits_df)

    tisserand_criterion_results, q_function_result = find_asteroids(cycler_orbits_df,
                                                                    asteroids_orbits_df)

    tisserand_criterion_results.head(100).to_csv('results/tisserand_criterion_result.csv')
    q_function_result.head(100).to_csv('results/q_function_result.csv')
