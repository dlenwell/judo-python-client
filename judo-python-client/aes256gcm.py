"""
Copyright 2020 David Lenwell, Judo Security inc

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
"""
aes256 gcm mode wrapper functions

"""
from base64 import b64encode
from binascii import hexlify
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Random import get_random_bytes
from Crypto.Protocol.secret_sharing import Shamir


class aes256gcm:
    """class aes256gcm
    """
    shares, string_shares = []
    kek, dek, shares, encryped_dek, encryped_data, kekHex, data = None


    def __init__(self, data):
        """__init__
        """

        self.kek = get_random_bytes(32)
        self.dek = get_random_bytes(32)
        self.data = data
        self.encryped_data = self.encrypt(self.data, self.dek)
        self.encryped_dek = self.encrypt(self.dek, self.kek)
        self.kekHex = b64encode(self.kek)


    def chop(self, min_shards, shards):
        string_shares = []
        self.shares = Shamir.split(min_shards, shards, self.kekHex)

        for share in shares:
            self.string_shares.append(hexlify(share))


    def encrypt(self, data, key):
        """encrypt
        """
        cipher = AES.new(key, AES.MODE_GCM)
        cipherdata, tag = cipher.encrypt_and_digest(data)
        # tag len : 16bytes
        return cipher.nonce + tag + cipherdata


    def decrypt(self, data):
        """decrypt
        """
        cipher = AES.new(self.key, AES.MODE_GCM, data[:16])
        try:
            phaindata = cipher.decrypt_and_verify(data[32:], data[16:32])
            return phaindata
        except ValueError as e:
            raise
