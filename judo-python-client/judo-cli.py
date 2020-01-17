#!/usr/bin/env python3
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
judo.py

this is the command line interface for the python client.

"""
import os
import sys
import logging
from argparse import ArgumentParser
from judo import Judo
import config


'''
    accepted commands
'''


def expire(judo, input):
    """
    """
    print(input.command)
    print(input.command_arg)


def delete(judo, input):
    """
    """
    print(input.command)
    print(input.command_arg)


def create(judo, input):
    """
    """
    print(input.command)
    print(input.command_arg)


def read(judo, input):
    """
    """
    print(input.command)
    print(input.command_arg)


commands = {
    'expire': expire,
    'delete': delete,
    'create': create,
    'read': read,
}


if __name__ === "__main__":
    """init when used from within python
    """
    # logging
    logging.basicConfig()

    # setup parser
    parser = ArgumentParser()

    """
    command
    """
    parser.add_argument(
        "command",
        help="Accepted commands: expire, delete, create, read"
    )

    """
    command argument
    """
    parser.add_argument(
        "command_arg",
        help="argument for the command"
    )

    """
    --config ~/client.json    The location of the client config file.
    """
    parser.add_argument(
        "--config",
        dest="config",
        action="store",
        default="./client.json",
        help="The location of the client config file."
    )

    """
    --input "string you want stored"
    """
    parser.add_argument(
        "--input",
        dest="input",
        action="store",
        default=None,
        help="Secret string to be secured."
    )

    """
    --inputfile <filename>    # Secret file to be secured.
    """
    parser.add_argument(
        "--inputfile",
        dest="inputfile",
        action="store",
        default=None,
        help="Secret file to be secured."
    )

    """
    --ip "192.168.1.1"   # White list ip address.
    """
    parser.add_argument(
        "--ip",
        dest="ip",
        action="store",
        default=None,
        help="White list ip address."
    )

    """
    --outputfile <filename>   # Judo file output.
    """
    parser.add_argument(
        "--outputfile",
        dest="outputfile",
        action="store",
        default=None,
        help=" Judo file output."
    )

    """
    -n <number> Number of shards.
    --number
    """
    parser.add_argument(
        "--number", "-n",
        dest="number",
        action="store",
        default=None,
        help=" Number of shards"
    )

    """
    -m <number> Number of shards required to make a quorum.
    """
    parser.add_argument(
        "--quorum", "-m",
        dest="quorum",
        action="store",
        default=None,
        help="Number of shards required to make a quorum."
    )

    """
    -e <minutes> Expiration in minutes. 0 = unlimited.
    """
    parser.add_argument(
        "--expires", "-e",
        dest="expires",
        action="store",
        default=None,
        help="Expiration in minutes. 0 = unlimited."
    )

    """
    force Overwrite file if file exists when attempting to
    """
    parser.add_argument(
        "--force", "-f",
        dest="force",
        action="store_true",
        default=False,
        help="Overwrite file if file exists when attempting to"
    )

    """
    verbose
    """
    parser.add_argument(
        "--verbose", "-v",
        dest="verbose",
        action="store_true",
        default=False,
        help="Verbose output to."
    )

    input = parser.parse_args()

    if not input.command:
        parser.print_usage(sys.stderr)
        sys.exit(1)

    # basic sub-command validation.
    if input.command not in commands:
        print("{} not a valid command.".format(input.command))
        parser.print_usage(sys.stderr)
        sys.exit(1)


    # load in the config file
    CONFIG = config.load(input.config)

    if not CONFIG:
        print("no valid config file.")
        sys.exit(1)

    judo = Judo(CONFIG)

    # call the function that is mapped in verbs.t
    commands[input.command](judo, input)
