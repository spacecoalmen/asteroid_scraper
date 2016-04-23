import argparse
import pprint
import pandas
from asteroid_scraper.finder import find_asteroids


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
        cycler_orbits_df = pandas.read_csv(_file)
        cycler_orbits = cycler_orbits_df.to_dict(orient="records")

    with open(opts.asteroid_file, 'r') as _file:
        asteroid_orbits_df = pandas.read_csv(_file)
        asteroid_orbits = asteroid_orbits_df.to_dict(orient="records")

    pprint.pprint(find_asteroids(cycler_orbits, asteroid_orbits))




