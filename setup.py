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

version = '0.1.1'

ext_modules = [Extension("donna25519._curve25519",
                         ["donna25519/donna25519module.c",
                          "curve25519-donna/curve25519-donna.c"],
                         )]

short_description="Python wrapper for the Curve25519-donna cryptographic library"
long_description="""\
Curve 25519 is an elliptic curve cryptography key-agreement protocol.

Two parties, Alice and Bob, first generate their (public, private) 
keypairs. They then exchange public keys on an insecure channel, and 
use the protocol to establish a shared secret between them.

This is a Python wrapper for the 'curve25519-donna' library for the 
curve 25519 elliptic curve Diffie-Hellman key exchange algorithm. The
portable C 'Donna' library was written by Adam Langley, and is hosted 
at https://github.com/agl/curve25519-donna. This library is a near-
complete rewrite of an earlier python wrapper written by Brian Warner 
of Mozilla.

Documentation is available at https://github.com/Muterra/donna25519.
"""

setup(name="donna25519",
      version=version,
      description=short_description,
      long_description=long_description,
      author="Nick Badger",
      url='https://github.com/Muterra/donna25519',
      author_email="badg@muterra.io",
      license="BSD",
      packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
      ext_modules=ext_modules,
      keywords='curve25519, curve 25519, donna, cryptography, ecdh, ecdhe, '
          'elliptic curve cryptography, ecc, diffie hellman, key agreement',
      # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 4 - Beta',

          # Indicate who your project is intended for
          'Intended Audience :: Developers',
          'Topic :: Security :: Cryptography',
          'Topic :: Software Development',
          'Topic :: Utilities',

          # Pick your license as you wish (should match "license" above)
          'License :: OSI Approved :: BSD License',

          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
      ],
      )
