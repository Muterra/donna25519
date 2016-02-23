# What the fork?

This is a fork of [AGL's existing repo](https://github.com/agl/curve25519-donna). There are three reasons it exists, in order:

1. Add proper [documentation](doc/readme.md) for python (**extremely** high priority, aka done for the existing library)
2. Fix unexpected behavior in python binding -- namely, make_shared should not force SHA-256 hashing of the shared secret (medium priority)
3. Allow for future building of binary wheel distributions, because I spent an entire morning trying to get proper compilation working on my windows box (low priority) 

That being said:

+ **Branch master:** Documentation update only, as of 23 Feb 2016
+ **Branch ymmv:** Remove prehashing of shared secret. Can be cloned and locally installed if you'd like.

These branches will only be merged when the wheel distribution is available. At that point they will also be made available on pip as donna25519. There is no expected ETA on that. If you'd like it sooner, pay Muterra to do it (seriously not a joke, we're grossly understaffed and time is money).

# curve25519-donna

*Note*: this code is from 2008. Since that time, many more, great implementations of curve25519 have been written, including several amd64 assembly versions by djb. You are probably better served now by [NaCl](http://nacl.cr.yp.to) or [libsodium](https://github.com/jedisct1/libsodium).

[curve25519](http://cr.yp.to/ecdh.html) is an elliptic curve, developed by [Dan Bernstein](http://cr.yp.to/djb.html), for fast [Diffie-Hellman](http://en.wikipedia.org/wiki/Diffie-Hellman) key agreement. DJB's [original implementation](http://cr.yp.to/ecdh.html) was written in a language of his own devising called [qhasm](http://cr.yp.to/qhasm.html). The original qhasm source isn't available, only the x86 32-bit assembly output.

Since many x86 systems are now 64-bit, and portability is important, this project provides alternative implementations for other platforms.

| Implementation       | Platform   | Author | 32-bit speed | 64-bit speed | Constant Time |
|----------------------|------------|--------|--------------|--------------|---------------|
| curve25519           | x86 32-bit | djb    | 265µs        | N/A          | yes           |
| curve25519-donna-c64 | 64-bit C   | agl    | N/A          | 215µs        | yes           |
| curve25591-donna     | Portable C | agl    | 2179µs       | 610µs        |               |

(All tests run on a 2.33GHz Intel Core2)

## Usage

The usage is exactly the same as djb's code (as described at http://cr.yp.to/ecdh.html) except that the function is called `curve25519\_donna`.

To generate a private key, generate 32 random bytes and:

```
mysecret[0] &= 248;
mysecret[31] &= 127;
mysecret[31] |= 64;
```

To generate the public key, just do:

```
static const uint8_t basepoint[32] = {9};
curve25519_donna(mypublic, mysecret, basepoint);
```

To generate a shared key do:

```
uint8_t shared_key[32];
curve25519_donna(shared_key, mysecret, theirpublic);
```

And hash the `shared\_key` with a cryptographic hash function before using.

For more information, see [djb's page](http://cr.yp.to/ecdh.html).

## Building

If you run `make`, two .a archives will be built, similar to djb's curve25519
code. Alternatively, read on:

## ESP8266

If you're interested in running curve25519 on an ESP8266, see [this project](https://github.com/CSSHL/ESP8266-Arduino-cryptolibs).
