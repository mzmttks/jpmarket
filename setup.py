from distutils.core import setup

setup(name = 'jpmarket',
      version = '0.1',
      description = 'pandas DataReader extension for Japanese market data',
      author = 'Takeshi Mizumoto',
      author_email='ta.mizumoto@gmail.com',
      license='New BSD',
      url = 'https://github.com/mzmttks/jpmarket',
      packages = ["jpmarket"]
      long_description = """
jpmarket
--------
This module provides a pandas.DataReader compatible method
for Japanese market data.

See https://github.com/mzmttks/jpmarket for details.
"""
     )
