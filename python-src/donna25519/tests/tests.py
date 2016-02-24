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

import unittest

from donna25519 import PrivateKey
from donna25519 import PublicKey

# Test vectors taken from NaCl distribution
# http://cr.yp.to/highspeed/naclcrypto-20090310.pdf

TVa = int.to_bytes(
    0x77076d0a7318a57d3c16c17251b26645df4c2f87ebc0992ab177fba51db92c2a,
    length=32,
    byteorder='big'
)
TVa_public = int.to_bytes(
    0x8520f0098930a754748b7ddcb43ef75a0dbf3a0d26381af4eba4a98eaa9b4e6a,
    length=32,
    byteorder='big'
)
TVb = int.to_bytes(
    0x5dab087e624a8a4b79e17f8b83800ee66f3bb1292618b6fd1c2f8b27ff88e0eb,
    length=32,
    byteorder='big'
)
TVb_public = int.to_bytes(
    0xde9edb7d7b7dc1b4d35b61c2ece435373f8343c85b78674dadfc7e146f882b4f,
    length=32,
    byteorder='big'
)
TVab = int.to_bytes(
    0x4a5d9d5ba4ce2de1728e3bf480350f25e07e21c947d19e3376f09b3c1e161742,
    length=32,
    byteorder='big'
)

# Manually clamp those test vectors
TVa_clamped = bytearray(TVa)
TVa_clamped[0] &= 248
TVa_clamped[31] &= 127
TVa_clamped[31] |= 64

TVb_clamped = bytearray(TVb)
TVb_clamped[0] &= 248
TVb_clamped[31] &= 127
TVb_clamped[31] |= 64

# class TestUnitPrivate(unittest.TestCase):
#     def test_init(self):
        
class TestPublicInit(unittest.TestCase):
    def setUp(self):
        ''' Test __init__ and create Alice and Bob from TVa, TVb above.
        '''
        self.alice = PublicKey(TVa_public)
        self.bob = PublicKey(TVb_public)
        
    def test_public_get(self):
        alice = self.alice.public
        bob = self.bob.public
        self.assertEqual(alice, TVa_public, 'Alice public vector mismatch')
        self.assertEqual(bob, TVb_public, 'Bob public vector mismatch')
        
    def test_public_set(self):
        ''' Ensure PublicKey.public is read-only.
        '''
        with self.assertRaises(AttributeError, 'alice.public failed set test'):
            self.alice.public = bytes(32)
        with self.assertRaises(AttributeError, 'bob.public failed set test'):
            self.bob.public = bytes(32)
        
    def test_public_set(self):
        ''' Ensure PublicKey.public is not deletable.
        '''
        with self.assertRaises(AttributeError, 'alice.public failed del test'):
            del self.alice.public
        with self.assertRaises(AttributeError, 'bob.public failed del test'):
            del self.bob.public
            
    def test_init_typecheck(self):
        ''' Test type checking on init.
        '''
        mv = memoryview(self.alice)
        with self.assertRaises(TypeError, 'PublicKey failed init type check.'):
            alice = PublicKey(mv)
        ba = bytearray(self.alice)
        with self.assertRaises(TypeError, 'PublicKey failed init type check.'):
            alice = PublicKey(ba)
        other = int.from_bytes(TVa_public)
        with self.assertRaises(TypeError, 'PublicKey failed init type check.'):
            alice = PublicKey(other)
            
    def test_init_lencheck(self):
        ''' Test length checking on init.
        '''
        less = bytes(31)
        with self.assertRaises(ValueError, 'PublicKey failed init len check.'):
            test = PublicKey(less)
            
        more = bytes(33)
        with self.assertRaises(ValueError, 'PublicKey failed init len check.'):
            test = PublicKey(more)
            
        edge = bytes()
        with self.assertRaises(ValueError, 'PublicKey failed init len check.'):
            test = PublicKey(edge)

# Unit tests
    # Test public first, since private requires it for basically everything
    # Include test vectors
    # Include reloading test vectors

# Integration tests

# Functional tests
    # Generate two random identities
    # Perform key exchange both ways
    # Ensure results match
    # Repeat a bunch of times

    # in1[0] &= 248;
    # in1[31] &= 127;
    # in1[31] |= 64;

if __name__ == "__main__":
    # unittest.main()
    import IPython
    IPython.embed()