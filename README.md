About asteroid_scraper
======================

Installing
==========

``asteroid_scraper`` can be installed using the setuptools script:

    $ python setup.py install

from inside the ``asteroid_scraper`` directory.
This will install the program system wide, running with ``sudo``,
might be required on some systems.

In case install process fails complaining about missing ``setuptools``,
you might be required to install ``python setuptools`` through your 
system package manager or you might download and install it manually 
with:

    $ wget https://bootstrap.pypa.io/ez_setup.py -O - | sudo python

> If the system runs other python software, to avoid messing with system
wide packages and dependencies, installing in a ``virtualenv`` is 
usually suggested. Additional information regarding python virtual 
environments can be found at: 
<http://docs.python-guide.org/en/latest/dev/virtualenvs/>

Running
=======

To run ``asteroid_scraper`` just use the ``scrape_asteroids`` command 
after install, you must provide *cycler orbits csv file* and *asteroids 
csv file* <http://ssd.jpl.nasa.gov/sbdb_query.cgi>, you can find sample 
files in the *example_files* folder:

    $ scrape_asteroids ./example_files/cycler_orbits.csv ./example_files/asteroids.csv \
    -o example_files/results/results.csv -l 500

> For a right **tisserand** and **Qfunction** column formatting take a 
> look at the the [CSV formatting section]
> (https://github.com//spacecoalmen/asteroid_scraper/blob/master/README.md#csv-format)

Command Line Options
--------------------
``scrape_asteroids`` script provides some options to filter 
**asteroids** and limit the output, you can filter **asteroids** 
directly on the [Nasa search engine]
(http://ssd.jpl.nasa.gov/sbdb_query.cgi), set some filters or use the 
defaults:

    usage: scrape_asteroids [-h] [-o OUTPUT] [-l LIMIT] [-a MIN_SEMIAX]
                            [-A MAX_SEMIAX] [-e MIN_ECCE] [-E MAX_ECCE]
                            [-i MIN_INCL] [-I MAX_INCL]
                            asteroids cycler

    Find asteroids that can be mined by the cycler

    positional arguments:
      asteroids             asteroids orbits csv file obtained at
                            http://ssd.jpl.nasa.gov/sbdb_query.cgi
      cycler                cycler orbits csv file

    optional arguments:
      -h, --help            show this help message and exit
      -o OUTPUT, --output OUTPUT
                            output file path
      -l LIMIT, --limit LIMIT
                            limit the top N matches
      -a MIN_SEMIAX, --min_semiax MIN_SEMIAX
                            asteroid minimun semiax
      -A MAX_SEMIAX, --max_semiax MAX_SEMIAX
                            asteroid maximum semiax
      -e MIN_ECCE, --min_ecce MIN_ECCE
                            asteroid minimum orbital eccentricity
      -E MAX_ECCE, --max_ecce MAX_ECCE
                            asteroid maximum orbital eccentricity
      -i MIN_INCL, --min_incl MIN_INCL
                            asteroid minimum incl (rad)
      -I MAX_INCL, --max_incl MAX_INCL
                            asteroid maximum incl (rad)


CSV format
==========

The *csv files* must have the following columns:

**cycler**

| key    | unit  | description            |
| ------ | ----  | ---------------------- |
| ecce   | **    |                        |
| incl   | *rad* |                        |
| Omega  | *rad* |                        |
| omegap | *rad* |                        |
| semiax | **    |                        |

**asteroids_orbits**

| key | unit  |  description          |
| --- | ----  | --------------------- |
| e   | **    |                       |
| i   | *deg* |                       |
| a   | **    |                       |
| om  | *deg* |                       |
| w   | *deg* |                       |
