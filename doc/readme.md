This documentation has been created and maintained by Muterra, Inc. Muterra retains the copyright to it, but it may be redistributed under the BSD license, as noted in LICENSE.md.

# donna25519 overview

Python bindings to Curve25519-Donna.

## Install and import:

```python
pip install curve25519-donna
import curve25519
```

Installation notes: installation currently requires the ability to compile C extensions. In Windows, this can be a lengthy process, especially for a 64-bit build: 

1. First install microsoft visual C++ 2010: http://filehippo.com/de/download_visualc_2010_express_edition/
2. Second, install microsoft .net framework 4. 
3. Install microsoft windows sdk 7.1: https://www.microsoft.com/en-us/download/details.aspx?id=8279
4. May need to do some version jiggerypokey like this: http://stackoverflow.com/a/33260090/5964816
5. In C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\bin\amd64, create file ```vcvars64.bat```, with the following contents:

```
CALL "C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin\SetEnv.cmd" /x64
```

## Usage:

This library provides two public classes:

+ ```Private```
+ ```Public```

### ```class Private(secret=None, seed=None)```

Generates an ECDH private key on Curve25519, using AGL's Curve25519-donna implementation. This will be properly clamped, ie, avoid the following three steps referenced by DJB, as they will already be performed:

```
mysecret[0] &= 248;
mysecret[31] &= 127;
mysecret[31] |= 64;
```

#### argument ```secret=None```

This value is directly passed to the underlying curve25519-donna library as the private key *d*. It must be securely random; for python, we suggest ```os.urandom()```, though this may be inappropriate for eg. servers, where entropy pools may deplete.

If you call ```Private()``` with no arguments, it will securely default to a secret obtained from ```os.urandom()```.

Secret must be a bytes object of length 32.

#### argument ```seed=None```

This value is passed through the following pseudorandom permutation to generate a private key *d*:

```python
secret = sha256(b"curve25519-private:" + seed).digest()
```

**We strongly recommend avoiding this argument entirely.** It still relies upon the entropy in the seed to generate the private key, and so it still should be suitably securely random. Passing ```os.urandom()``` to ```secret``` is a much preferable choice.

If ```secret``` is passed to the constructor, ```seed``` must not be.

Seed must be a bytes object of length 32.

#### ```Private().serialize()```

Returns a bytes representation of the private key. **This function violates SEC 1 v2.0; it does not return the value with ASN.1 DER/PEM formatting, and instead returns a raw integer.** It is exactly equivalent to ```Private().private```.

Return length is 32 bytes.

#### ```Private().get_public()```

Returns the corresponding public key as a ```Public()``` instance.

#### ```Private().get_shared_key(public, hashfunc=None)```

Performs a key exchange between ```Private()``` and ```public```, resulting in a shared secret. Outputs a bytes object of length 32. This shared secret should always be passed to an appropriate key derivation function before use. In this context, hashing may be an appropriate KDF.

```hashfunc``` will pre-hash the resulting secret before returning it. **Note that, counter-intuitively, if it is left as ```None```, it will be passed through hashlib's SHA-256 before return.** If you would like the raw secret to pass to your own KDF, it is probably easiest to define a no-op hash function, for example:

```python
noop = lambda x: x
Private().get_shared_key(public, hashfunc=noop)
```

### ```class Public(public)```

Stores an ECDH public key.

#### argument ```public```

The ECDH/Curve25519 public key. Must be a bytes object of length 32.

#### ```Public().serialize()```

Returns a bytes representation of the public key. **This function violates SEC 1 v2.0; it does not return the value with ASN.1 DER/PEM formatting, and instead returns a raw integer.** It is exactly equivalent to ```Public().public```.

Return length is 32 bytes.
