#! /usr/bin/python

from setuptools import setup, Extension

version = '0.1a1'

ext_modules = [Extension("curve25519._curve25519",
                         ["python-src/curve25519/curve25519module.c",
                          "curve25519-donna.c"],
                         )]

short_description="Python wrapper for the Curve25519 cryptographic library"
long_description="""\
Curve25519 is a fast elliptic-curve key-agreement protocol, in which two
parties Alice and Bob each generate a (public,private) keypair, exchange
public keys, and can then compute the same shared key. Specifically, Alice
computes F(Aprivate, Bpublic), Bob computes F(Bprivate, Apublic), and both
get the same value (and nobody else can guess that shared value, even if they
know Apublic and Bpublic).

This is a Python wrapper for the portable 'curve25519-donna' implementation
of this algorithm, written by Adam Langley, hosted at
https://github.com/agl/curve25519-donna

Documentation is available at https://github.com/Muterra/curve25519-donna
"""

setup(name="donna25519",
      version=version,
      description=short_description,
      long_description=long_description,
      author="Nick Badger, Brian Warner",
      url='https://github.com/Muterra/curve25519-donna',
      author_email="badg@muterra.io",
      license="BSD",
      packages=["curve25519", "curve25519.test"],
      package_dir={"curve25519": "python-src/curve25519"},
      ext_modules=ext_modules,
      # keywords='smartyparse, data structure, dynamic, binary, parser, builder, pack, unpack',
      # # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
      # classifiers=[
      #     # How mature is this project? Common values are
      #     #   3 - Alpha
      #     #   4 - Beta
      #     #   5 - Production/Stable
      #     'Development Status :: 3 - Alpha',

      #     # Indicate who your project is intended for
      #     'Intended Audience :: Developers',
      #     'Topic :: Software Development',
      #     'Topic :: Utilities',

      #     # Pick your license as you wish (should match "license" above)
      #     'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',

      #     # Specify the Python versions you support here. In particular, ensure
      #     # that you indicate whether you support Python 2, Python 3 or both.
      #     'Programming Language :: Python :: 3',
      #     'Programming Language :: Python :: 3.3',
      #     'Programming Language :: Python :: 3.4',
      #     'Programming Language :: Python :: 3.5',
      # ],
      )
