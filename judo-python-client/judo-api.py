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

 - Delete a secret

0.1.0
POST
/secret/:secretId/DeleteSecret
Parameter

Field	Type	Description
secretId	String
Secret Id.
"""
import logging
import httpx

from types import MethodType

from .exceptions import ActionNotFound, ActionURLMatchError, MissingParams
from .models import Request, Methods
from .request import make_async_request, make_request

logger = logging.getLogger(__name__)


class JudoApi():
    """api request wrapper
    """
    params, headers = {}
    timeout = False

    """
    storage_key property
    """
    _storage_key = None
    @property
    def storage_key(self):
        return self._storage_key

    @storage_key.setter
    def storage_key(self, value):
        self._storage_key = value

    """
    organization_id property
    """
    _organization_id = None
    @property
    def organization_id(self):
        return self._organization_id

    @organization_id.setter
    def organization_id(self, value):
        self._organization_id = value

    """
    api_url property
    """
    _api_url = None
    @property
    def api_url(self):
        return self._api_url

    @api_url.setter
    def api_url(self, value):
        self._api_url = value

    """
    status property
    """
    _status = None
    @property
    def status(self):
        return self._status

    """
    params property
    """
    _params = {}
    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value


    def __init__(self, organization_id, storage_key, root_url):
        """
        """
        self._organization_id = organization_id
        self._storage_key = storage_key
        self._api_url = root_url


    def request_url(self, action, **kwargs):
        """
        
        """
        try:
            return(action['uri'].format(**kwargs))
        except IndexError:
            missing = []
            for param, type in action['uri_params'].items();
                if 'errormessage' not in kwargs:
                    missing.append('param')

            raise ActionURLMatchError(
                'Missing required url params',
                missing
            )

        return url


    def get_action(self, action_name):
        """

        """
        try:
            return Methods[method]
        except KeyError:
            raise ActionNotFound('method "{}" not found'.format(method))


    def set_params(self, action, **kwargs):
        """

        """
        to_return = {}
        missing = []

        for param, type in action['post_params']:
            if param not in kwargs:
                missing.append(key)
            else:
                to_return['param'] = kwargs.get(param)

        if 'post_params_optional' in action:
            for param, type in action['post_params']:
                if param in kwargs:
                    to_return['param'] = kwargs.get(param)

        if len(missing):
            raise MissingParams(missing)
        else:
            return(to_return)


    def action(self, action_name, **kwargs):
        """

        """
        self.params = self.set_params(action, **kwargs)
        action = self.get_action(action_name)

        request = Request(
            url=self.request_url(action, **kwargs),
            method=action['method'],
            params=self.params,
            headers=self.headers,
            timeout=self.timeout,
            kwargs=kwargs,
        )
        request.params.update(self.params)
        request.headers.update(self.headers)

        return make_request(self.client, request)
