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
"""
functions and template for creating a judo file
"""


def JudoFile(created, version, type, name,
             secret_id, index, n, m, wrapped_key, data):

    return json.dumps({
        "created": created,
        "version": version,
        "type": type,
        "name": name,
        "secret_id": secret_id,
        "index": index,
        "n": n,
        "m": m,
        "wrapped_key": wrapped_key,
        "data": data
    })
