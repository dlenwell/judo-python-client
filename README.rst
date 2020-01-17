==================
judo-python-client
==================


judosecurity.com


Description
===========
A python client for judo security

performs the following steps

1. Encrypt the "secret".
  - Create a DEK (32 random bytes).
  - Encrypt the "secret" (we use aes-256) using the DEK.
  - Create a KEK (32 random bytes).
  - Encrypt the DEK (aes-256) using the KEK.
2. Use shamir to split the KEK into multiple shards.
3. API call: Reserve a secret. If you broke your secret into 5 shards you
   should reserve a secret for 5 shards.
4. Keep note of the URLs returned from the API endpoint. You will write and
   eventually read from these URLs. You won't be able to request these URLs again.
5. Create a GUID to use as a TransactionID.
6. Upload each of the shards to one of the URLs received using the
   Shard/Upload Shard API call.
7. Mark the secret as fulfilled by calling the Fulfull secret API call.
8. Create a Judo file or store information so you can retrieve and decrypt
   the secret later. Our client creates a Judo file. You can see an example
   of a Judo file in the next section.
