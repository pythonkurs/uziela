from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(name='uziela',
      version=version,
      scripts = ['scripts/getting_data.py', 'scripts/check_repo.py'],
      description="package for python course",
      long_description="""\
package for python course where I will put my code""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='pythonkurs',
      author='Karolis Uziela',
      author_email='karolis.uziela@scilifelab.se',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "untangle",
          "requests",
          "dateutil",
          "pandas",
          "getpass",
          "collections",
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
