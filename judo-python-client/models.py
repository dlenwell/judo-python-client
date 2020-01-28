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
from collections import namedtuple
import String
import Integer


Request = namedtuple("Request", ["url", "method", "params", "body",
                                 "headers", "timeout", "kwargs"])
Response = namedtuple("Response", ["url", "method", "body", "headers",
                                   "status_code", "client_response"])

Secret = ""

Actions = {
    'CreateSecret': {
        'method': 'POST',
        'uri': '/organization/{organizationId}/CreateSecret',
        'uri_params': {
            'organizationId': String,
        },
        'post_params': {
            'description': "string",
            'numberOfShards': Integer,
            'expiresIn': 'integer'
        },
        'post_params_optional': {
            'allowedIPs': 'list'
        }
    },
    'DeleteSecret': {
        'method': 'POST',
        'uri': '/secret/{secretId}/DeleteSecret',
        'uri_params': {'secretId': 'string'},
    },
    'ExpireSecret': {
        'method': 'POST',
        'uri': '/secret/{secretId}/ExpireSecret',
        'uri_params': {'secretId': 'string'},
    },
    'FulfillSecret': {
        'method': 'POST',
        'uri': '/secret/{secretId}/FulfillSecret',
        'uri_params': {'secretId': 'string'},
    },
    'GetShard': {
        'method': 'GET',
        'uri': "/shard/{shardId}?s={secretId}&t={transactionId}",
        'uri_params': {
            'shardId': 'string',
            'secretId': 'string',
            'transactionId': 'string'
        }
    },
    'SetShard': {
        'method': 'POST',
        'uri': "/shard/{shardId}?s={secretId}&t={transactionId}",
        'uri_params': {
            'shardId': 'string',
            'secretId': 'string',
            'transactionId': 'string'
        },
        'post_params': {
            'data': 'string'
        }
    },
    'EnableUser': {
        'method': 'POST',
        'uri': '/user/{userId}/Enable',
        'uri_params': {'userId': 'string'}
    }
}
