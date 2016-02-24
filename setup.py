'''
LICENSING
-------------------------------------------------

Copyright (c) 2016, Muterra Inc.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of Muterra Inc nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL MUTERRA INC BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

------------------------------------------------------
'''

#! /usr/bin/python

from setuptools import setup, Extension, find_packages

version = '0.1.0'

ext_modules = [Extension("donna25519._curve25519",
                         ["donna25519/donna25519module.c",
                          "curve25519-donna/curve25519-donna.c"],
                         )]

short_description="Python wrapper for the Curve25519-donna cryptographic library"
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
      author="Nick Badger",
      url='https://github.com/Muterra/donna25519',
      author_email="badg@muterra.io",
      license="BSD",
      packages=find_packages(exclude=['contrib', 'doc', 'tests*']),
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
