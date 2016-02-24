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

Complete rewrite of code originally written by Brian Warner.
'''

from . import _curve25519
import os

class PrivateKey():
    def __init__(self, secret=None):
        ''' Creates a **new** PrivateKey from an optional secret. Do not
        use this for loading existing keys!
        '''
        # Generate secret if none is passed
        if secret is None:
            secret = os.urandom(32)
        
        # Type check. I'd like to duck type, but the C binding doesn't support
        # it (at least for now).
        if not isinstance(secret, bytes):
            raise TypeError('Secret must be bytes object.')
        if len(secret) != 32:
            raise ValueError('Secret must be 32 bytes long.')
            
        self._private = _curve25519.make_private(secret)
            
    @classmethod
    def load(cls, private):
        ''' Loads a PrivateKey from an existing private key.
        '''
        # To hell with performance! Use the constructor to test validity.
        # Yeah, okay, I'm just being lazy
        self = cls(private)
        self._private = private
        return self
        
    @property
    def private(self):
        ''' Read-only to help insulate accidental deletions and modifications.
        '''
        return self._private

    def get_public(self):
        return PublicKey(_curve25519.make_public(self.private))

    def do_exchange(self, public_key):
        if not isinstance(public_key, PublicKey):
            raise TypeError('"public_key" must be an instance of PublicKey.')
            
        shared = _curve25519.make_shared(self.private, public_key.public)
        return shared

class PublicKey():
    def __init__(self, public):
        if not isinstance(public, bytes):
            raise TypeError('Argument "public" must be bytes object.')
        if len(public) != 32:
            raise ValueError('Argument "public" must be 32 bytes long.')
            
        self._public = public
        
    @property
    def public(self):
        ''' Read-only to help insulate accidental deletions.
        '''
        return self._public