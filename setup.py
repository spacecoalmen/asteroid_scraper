from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.md')).read()
except IOError:
    README = ''

version = "0.0.1"

INSTALL_REQUIREMENTS = [
      'numpy==1.11.0',
      "pandas==0.18.0"
]

setup(name='asteroid_scraper',
      version=version,
      description="",
      long_description=README,
      classifiers=[],
      keywords='',
      author='Carbonai dello Spazio',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=INSTALL_REQUIREMENTS,
      entry_points={
            'console_scripts': [
                  'scrape_asteroids = asteroid_scraper.__main__:main',
            ]
      }
      )
