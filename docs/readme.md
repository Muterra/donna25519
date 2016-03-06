# donna25519 overview

Python bindings to Curve25519-Donna.

## Install and import:

(Eventually) from Pip:

```
pip install donna25519
```

From source:

```
git clone https://github.com/Muterra/donna25519
pip install .
```

Importing:

```python
import donna25519
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