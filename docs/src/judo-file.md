#Example Judo File#

`created:`    Date/Time the Judo file was created

`version:`    The version of the Judo file.

`type:`       1 = string secret, 2 = file secret

`name:`       The friendly name of the secret.

`secret_id:`  The id of the secret. This information comes back from
              the "Reserve Secret" endpoint.

`index:`       The shard URLs.

`n:` The number of shards.

`m:` The minimum number of shards required to recreate the secret.

`wrapped_key:` The encrypted DEK.

`data:` The encrypted secret.

  {
      "created": "11/15/2019, 9:23:36 AM",
      "version": 1,
      "type": 1,
      "name": "Database password",
      "secret_id": "5d093294-2725-4a29-948a-ba13d648f5f0",
      "index": [
          "http://localhost/store_1/shard/784837a9-7407-4ec4-a4f9-6dc0080d59c1",
          "http://localhost/store_2/shard/8bc9d982-c318-44e5-83dd-f12ff4c0b2d8",
          "http://localhost/store_1/shard/25ab53ed-0495-4c36-aa38-c7baefbb8842",
          "http://localhost/store_2/shard/6c74ef8d-ac14-4b49-a884-361adec1b9cf",
          "http://localhost/store_1/shard/ceb365fb-c7ff-4d4a-b172-b2ad9b2aee7c"
      ],
      "n": 5,
      "m": 3,
      "wrapped_key": "mR3+Aa4tWYY2xt8Q0iJNofT8DN3Pj1reGX1QUGjD75YtpwOqDIDB3k4dbx7DBuVRetdce/JP0xtwrvl1BUcVUw==",
      "data": "aYANqMgUPUzW9xRQU6a9ipwWQSHpr1cknm+BSMG20BUO1+68yIQ="
  }
