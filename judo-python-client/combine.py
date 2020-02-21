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
from encryption import decrypt
from binascii import unhexlify
from Crypto.Protocol.SecretSharing import Shamir


def combine(shards, judo_file):
    """combine

    this class is passed the
    """
    # Recombine the shards to create the kek
    combined_shares = Shamir.combine(shards)
    combined_shares_string = "{}".format(combined_shares)

    # decrypt the dek uysing the recombined kek
    decrypted_dek = decrypt(
        judo_file['wrappedKey'],
        unhexlify(combined_shares_string)
    )

    # decrypt the data using the dek
    decrypted_data = decrypt(
        judo_file['data'],
        unhexlify(decrypted_dek)
    )

    decrypted_text = unhexlify(decrypted_data)

    return(decrypted_data, decrypted_text)
