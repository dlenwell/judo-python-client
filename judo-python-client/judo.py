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
import json
from uuid import uuid4
from base64 import b64encode
from judo_api import JudoApi
from chop import Chop
from combine import combine
from judofile import JudoFile
from urllib import request


"""
judo.py

imoprtable api wrapper object.

"""


class Judo():
    """Judo Python Class

    Can be imported and used from other python apps..
    is consumed by judo-cli.py
    """
    @property
    def storage_key(self):
        """
        """
        return self._storage_key

    @storage_key.setter
    def storage_key(self, value):
        """
        """
        self._storage_key = value

    @property
    def organization_id(self):
        """
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, value):
        """
        """
        self._organization_id = value

    @property
    def api_url(self):
        """
        """
        return self._api_url

    @api_url.setter
    def api_url(self, value):
        """
        """
        self._api_url = value

    @property
    def output_path(self):
        """
        """
        return self._output_path

    @output_path.setter
    def output_path(self, value):
        """
        """
        self._output_path = value

    def __init__(self, CONFIG=None, organization_id=None, storage_key=None,
                 api_url=None):
        """init function
        """
        if CONFIG:
            self.organization_id = CONFIG['organizationId']
            self.storage_key = CONFIG['storageKey']
            self.api_url = CONFIG['apiUrl']
        else:
            if organization_id:
                self.organization_id = organization_id
            if storage_key:
                self.storage_key = storage_key
            if api_url:
                self.api_url = api_url

        if self.organization_id and self.api_url and self.storage_key:
            self.init_api()

    def init_api(self):
        """connect to the judo api
        """
        self.api = JudoApi(organization_id=self.organization_id,
                           storage_key=self.storage_key,
                           root_url=self.api_url)

    def read_judo_file(self, input_file):
        """read_judo_file
        """
        try:
            with open(input_file) as json_file:
                return(json.load(json_file))
        except ValueError:
            return {}

    def read_input_file(self, input_file):
        """read_input_file
        """
        try:
            with open(input_file) as secret:
                return(b64encode(secret))
        except ValueError:
            return {}

    def write_judo_file(self, outputfile=None):
        """write_judo_file

        TODO
        """
        return

    def create(self, secret_name, shards=5, input=None,
               min_shards=3, input_file=None,
               expiration=0, allowed_ips=None):
        """create secret
        """
        # define start time

        # validate IPs
        valid_ips = allowed_ips  # Todo make this actually validate list

        if input and input_file:
            pass
            # TODO: throw exception

        secret_file_name = ''
        if input:
            secret = input
            secret_type = 1

        elif input_file:
            secret = self.read_input_file(input_file)
            secret_file_name = input_file.rsplit('/')[0]
            secret_type = 2

        judo = Chop(secret)

        # split apart the kek using shamirs
        shards = judo.chop(self, min_shards, shards)

        # reserve the secret reserveSecret
        response = self.api.action(
            'CreateSecret', **{
                'organizationId': self.organization_id,
                'description': secret_name,
                'numberOfShards': shards,
                'expiresIn': expiration,
                'allowedIPs': valid_ips
            }
        )

        if response:
            # fillShards
            self.api.action('fillShards', (response.secretId,
                                           response.urls,
                                           judo.string_shares,
                                           self.storage_key))

            # fulfillSecret
            self.api.action('fulfillSecret', (response.secretId,
                                              self.storage_key))

            # write file to specified path
            self.write_judo_file(JudoFile({
                'version': 1,
                'type': secret_type,
                'filename': secret_file_name,
                'name': secret_name,
                'secretId': response.secretId,
                'index': response.urls,
                'n': shards,
                'm': min_shards,
                'wrapped_key': judo.encryped_dek,
                'data': judo.encryped_data
            }))

        # log the time taken
        # # TODO: finish time logging

    def delete(self, input_file):
        """delete
        """
        judo_file = self.read_judo_file(input_file)

        # fulfillSecret
        self.api.action('DeleteSecret', **{'secretId': judo_file['secretId']})

    def expire(self, input_file):
        """expire
        """
        judo_file = self.read_judo_file(input_file)

        # fulfillSecret
        self.api.action('ExpireSecret', **{'secretId': judo_file['secretId']})

    def get_shards(self, secret_id, urls):
        """get_shards

        downloads shards and combines them
        """
        transaction_id = uuid4()
        data = []

        for _url in urls:
            url = "{}?s={}&t={}".format(_url, secret_id, transaction_id)

            get = request.urlopen(
                url,
                headers={'Authorization': self.storage_key},
                method="get"
            )

            data.append(get.read())

        return(data)

    def read(self, input_file, force=False):
        """read

        reads in a judo file and attempts to decrypt the secret from available
        shards.
        """
        judo_file = self.read_judo_file(input_file)
        output_file = judo_file['filename']
        secret_type = judo_file['type']
        secret_id = judo_file['secretId']
        urls = judo_file['index']

        # get the shards
        shards = self.get_shards(secret_id, urls)

        # combine magic
        result, result_string = combine(shards, judo_file)

        if secret_type == 2:
            file = open(output_file, 'w')
            file.write(result)
            file.close()
        else:
            print('Decrypted secret: {}'.format(result_string))
