About asteroid_scraper
======================

Installing
==========

``asteroid_scraper`` can be installed using the setuptools script::

    $ python setup.py install

from inside the asteroid_scraper directory.
This will install the program system wide, running with ``sudo``,
might be required on some systems.

In case install process fails complaining about missing ``setuptools``,
you might be required to install ``python setuptools`` through your system
package manager or you might download and install it manually with::

    $ wget https://bootstrap.pypa.io/ez_setup.py -O - | sudo python

.. note::

    If the system runs other python software, to avoid messing with system
    wide packages and dependencies, installing in a ``virtualenv`` is usually
    suggested. Additional information regarding python virtual environments
    can be found at: http://docs.python-guide.org/en/latest/dev/virtualenvs/


Running
=======

To run ``asteroid_scraper`` just use the ``scrape_asteroids`` command after install::

    $ scrape_asteroids -c ./example_files/cycler_orbits.csv -m ./example_files/asteroids.csv

