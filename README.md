About asteroid_scraper
======================

``asteroid_scraper`` is a python software that allows to discover
asteroids eligible for mining, it computes **tisserand** and 
**Qfunction** algorithms to evaluate the asteroid's orbit compared to 
the **cycler** orbit, it's based on [**pandas Data Analysis Library**]
(http://pandas.pydata.org/)

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

    usage: scrape_asteroids [-h] [-o OUTPUT] [-l LIMIT]
                            [-s {tisserand,q_function}] [-a MIN_SEMIAXIS]
                            [-A MAX_SEMIAXIS] [-e MIN_ECCENTRICITY]
                            [-E MAX_ECCENTRICITY] [-i MIN_INCLINATION]
                            [-I MAX_INCLINATION]
                            cycler asteroids
    
    Find asteroids eligible to be mined by the cycler
    
    positional arguments:
      cycler                cycler orbits .csv file
      asteroids             asteroids orbits .csv file obtained at
                            http://ssd.jpl.nasa.gov/sbdb_query.cgi
    
    optional arguments:
      -h, --help            show this help message and exit
      -o OUTPUT, --output OUTPUT
                            output .csv file path
      -l LIMIT, --limit LIMIT
                            limit the top N matches
      -s {tisserand,q_function}, --sort_key {tisserand,q_function}
                            sort by tisserand delta or q_function delta
      -a MIN_SEMIAXIS, --min_semiaxis MIN_SEMIAXIS
                            asteroid minimum semi major axis
      -A MAX_SEMIAXIS, --max_semiaxis MAX_SEMIAXIS
                            asteroid maximum semi major axis
      -e MIN_ECCENTRICITY, --min_eccentricity MIN_ECCENTRICITY
                            asteroid minimum orbital eccentricity
      -E MAX_ECCENTRICITY, --max_eccentricity MAX_ECCENTRICITY
                            asteroid maximum orbital eccentricity
      -i MIN_INCLINATION, --min_inclination MIN_INCLINATION
                            asteroid minimum inclination to ecliptic (rad)
      -I MAX_INCLINATION, --max_inclination MAX_INCLINATION
                            asteroid maximum inclination to ecliptic (rad)


CSV format
==========

The *csv files* must have the following columns:

**cycler**

| key    | unit  | description             |
| ------ |:-----:| ----------------------- |
| ecce   |       | orbital eccentricity    |
| incl   | *rad* | inclination to ecliptic |
| Omega  | *rad* | longitude of Omega      |
| omegap | *rad* |                         |
| semiax | *AU*  | semi major axis         |

**asteroids_orbits**

| key | unit  | description             |
| --- |:-----:| ----------------------- |
| e   | **    | orbital eccentricity    |
| i   | *deg* | inclination to ecliptic |
| om  | *deg* | longitude of Omega      |
| w   | *deg* |                         |
| a   | *AU*  | semi major axis         |


Examples
========

Scrape using default filters, limit output to 500 matches, sort by 
**tisserand delta** column:

    $ scrape_asteroids ./example_files/cycler_orbits.csv ./example_files/asteroids.csv \
      -o example_files/results/500_tisserand_sorted_.csv -l 500 -s tisserand
      
Scrape using default_filter, limit output to 500 matches, sort by 
**q_function delta** column:

    $ scrape_asteroids ./example_files/cycler_orbits.csv ./example_files/asteroids.csv \
      -o example_files/results/500_q_function_sorted_.csv -l 500 -s q_function
      
Scrape using custom filter, limit output to 500 matches, sort by 
**q_function delta** column:

    $ scrape_asteroids ./example_files/cycler_orbits.csv ./example_files/asteroids.csv \
      -o example_files/results/custom_filters_500_q_function_sorted_.csv -l 500 -s q_function \
      -a 1.0 -A 1.7 -e 0 -E 0.45 -i 0.0 -I 0.35
