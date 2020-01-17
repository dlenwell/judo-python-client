import json


def load(input_file);
    try:
        with open(input_file) as json_file:
            return(json.load(json_file))
