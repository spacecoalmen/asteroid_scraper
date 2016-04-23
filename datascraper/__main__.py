import argparse
import pprint



def main():

    parser = argparse.ArgumentParser(
        description="Parse nasa csv data"
    )

    parser.add_argument('-f', '--file',
                        help='csv file')

    opts = parser.parse_args()

    with open(opts.file,'r') as file:
        lines = file.readlines()

        for line in lines:
            pprint.pprint(line)

    result = "ciao"

    pprint.pprint(result)

