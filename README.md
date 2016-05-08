[![Code Climate](https://codeclimate.com/github/Muterra/donna25519/badges/gpa.svg)](https://codeclimate.com/github/Muterra/donna25519)
[![Build Status](https://travis-ci.org/Muterra/donna25519.svg?branch=master)](https://travis-ci.org/Muterra/donna25519)

# Two important notes

1. be sure to run the output of the shared secret agreement through an appropriate KDF before use. A good hash function may suffice.
2. The C implementation of Curve25519 that this uses was written in 2008. A lot has changed since then. If you're just looking for something that does elliptic curve Diffie-Hellman and heard you should use curve25519, you're probably significantly better served by [NaCl](https://nacl.cr.yp.to) or [libsodium](https://github.com/jedisct1/libsodium). Also take a look at PyCA's [cryptography](https://cryptography.io) project.

# Installing and importing

**Supported python: 3.3+**. Tested on Windows and Linux.

**Installing:**

```
pip install donna25519
```

**Importing:**

```python
import donna25519
```

### Windows (Python 3.3)

Windows builds on python3.3 will require the ability to compile C extensions. Generally, that means you need Microsoft Visual C++. See [here](https://packaging.python.org/en/latest/extensions/#setting-up-a-build-environment-on-windows).

### Windows (Python 3.4+)

Donna25519 ships with compiled binary wheels for Windows. In other words, **you do not need additional software to compile Donna25519.** However, **due to a bug in pip you may need to update it before installing** by running ```python -m pip install --upgrade pip```. **Do** issue the command exactly like that, or you may run into permissions errors. Once pip is upgraded, install via pip as per above.

### Linux (Python 3.3+)

Donna25519 must be compiled from source on Linux. For that, you will need a compiler. On Ubuntu (or other Debian distros) you should only need ```sudo apt-get install build-essential python3-dev```.

### OSX

As with Linux, you will be compiling from source and need to build C code. Unfortunately we don't have any experience to share here.

**Note:** this library is *wholly untested* on Mac. It should work, but we haven't observed it doing so. If you get it running, we would be ecstatic to know.

# What the fork?

This is an almost-square-1-rewrite of Brian Warner's python bindings to [AGL's curve25519-donna C implementation](https://github.com/agl/curve25519-donna). Documentation for python usage can be found in [/doc](/doc). 

The original Warner cython bindings remain mostly unchanged for the moment, but the python wrapping has been 100% rewritten, for the following reasons:

1. Test all functions against NaCl test vectors, and generally provide better testing coverage
2. Remove unexpected post-key-agreement mandatory SHA256 behavior in python binding
3. Remove insecure use of assert when performing checks (optimizing compilers ignore it)
4. Binary wheel distributions for Windows
5. API improvement and documentation

Regarding support for Python 2: I believe the C binding supports it, but the Python wrapper does not. Though to be fair, that's entirely untested waters, so it's possible it would be easy to backport. That is, however, not a priority right now.

# Usage:

This library provides two public classes:

+ ```PrivateKey```
+ ```PublicKey```

### ```class PrivateKey(secret=None)```

Generates an ECDH private key on Curve25519, using AGL's Curve25519-donna implementation. This will be properly clamped, ie, avoid the following three steps referenced by DJB, as they will already be performed:

```
mysecret[0] &= 248;
mysecret[31] &= 127;
mysecret[31] |= 64;
```

**Do not use this to load existing private keys; your key will be wrong!** Use ```PrivateKey.load()``` instead.

#### argument ```secret=None```

This value is directly passed to the underlying curve25519-donna library as the private key *d*. It must be securely random; for python, we suggest ```os.urandom()```, though this may be inappropriate for eg. servers, where entropy pools may deplete.

If you call ```PrivateKey()``` with no arguments, it will securely default to a secret obtained from ```os.urandom()```.

Secret must be a bytes object of length 32.

#### classmethod ```PrivateKey.load(private)```

Loads an existing ECDH/Curve25519 private key. If loading from a different library or serialized key, ensure that the value has already been clamped, as explained above. If loading from this library, ```private``` should be the same value as was previously available from ```PrivateKey().private```.

#### ```PrivateKey().private```

Read-only attribute returning the ECDH/Curve25519 private key as a bytes object.

#### ```PrivateKey().get_public()```

Returns the corresponding public key as a ```PublicKey()``` instance.

#### ```PrivateKey().do_exchange(public)```

Performs a key exchange between ```PrivateKey()``` and ```public```, resulting in a shared secret. Outputs a bytes object of length 32. This shared secret should always be passed to an appropriate key derivation function before use. In this context, hashing may be an appropriate KDF.

```public``` must be a PublicKey instance.

### ```class PublicKey(public)```

Stores an ECDH public key.

#### argument ```public```

The ECDH/Curve25519 public key. Must be a bytes object of length 32.

#### ```PublicKey().public```

Read-only attribute returning the ECDH/Curve25519 public key as a bytes object.