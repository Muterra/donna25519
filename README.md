# What the fork?

This is a reorganization and rewrite of Brian Warner's python bindings to [AGL's curve25519-donna C implementation](https://github.com/agl/curve25519-donna). Please read his readme (follow that link) before use. Documentation for python usage can be found in [/doc](/doc). 

The original Warner *bindings* (aka glue Cython) remain (currently) mostly unchanged, but the python code has been entirely rewritten. There are several reasons this rewrap exists, in order:

1. Add proper [documentation](/python-src/doc/readme.md) for python (**extremely** high priority)
2. Test all functions against NaCl test vectors, and generally provide better testing coverage (high priority)
3. Fix unexpected behavior in python binding -- namely, make_shared should not force SHA-256 hashing of the shared secret (medium priority)
4. Fix several python security vulnerabilities, ex use of assert (medium priority)
5. Allow for future building of binary wheel distributions, because I spent an entire morning trying to get proper compilation working on my windows box (low priority) 
6. Various other API tweaks and things (low priority)

**All of the above have been completed, except binary wheel distributions.** This repo can be cloned and installed via 

```
git clone https://github.com/Muterra/curve25519-donna
pip install .
```

At some point in the near-ish-maybe future, this will be made available on pip as ```pip install donna25519```, including the binary wheels, to avoid compilation issues. There is no expected ETA on that. If you'd like it sooner, pay Muterra to do it (seriously not a joke, we're grossly understaffed and time is money). This is also true of Python 2 support; I believe the C binding supports it, but the Python wrapper does not.