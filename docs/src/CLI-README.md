# Judo Python Client - CLI

### Requirements
uses python 3


```
python3 setup.py install
```

### Client Setup
- Create a `client.json` configuration file with the contents.
```
{
  "organizationId": "",
  "storageKey": "",
  "api_root_url": "<url>"
}
```
- Login to the judo website.
- If you see an organization Id copy the `organization Id` from your profile view into the config file.
- Copy the `Storage Key` from your profile view into the config file.
- Save the changes to the client.json file.


### Usage
You can issue the command `judo` to see how to use the client. Here is an overview:
```
Creating a new Judo file from an input string:
  judo create <name> --outputfile <filepath>  --input <secret> -n 5 -m 3 -e 0

Creating a new Judo file from an input file:
  judo create <name> --outputfile <filepath> --inputfile  <filepath>  -n 5 -m 3 --expires 0

Reading a Judo file:
  judo read <filepath>

Expire an existing Judo secret:
  judo expire <filepath>

Delete an existing Judo secret:
  judo delete <filepath>


  -h, --help              show this help message and exit
  --config <filepath>     The location of the client config file.

  --input INPUT           Secret string to be secured.
  --inputfile <filepath>  Secret file to be secured.
  --ip <ip address>       White list ip address.
  --outputfile <filepath> Judo file output.
  --number <integer>      Number of shards
  -n <integer>            
  --quorum <integer>      Number of shards required to make a quorum.
  -m <integer>

  --expires <integer>     Expiration in minutes. 0 = unlimited.
  -e <integer>

  --force, -f             Overwrite file if file exists when attempting to
  --verbose, -v           Verbose output.
```
