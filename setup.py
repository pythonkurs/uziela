from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='uziela',
      version=version,
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
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
