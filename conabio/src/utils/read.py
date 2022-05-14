import json


def read_json(path):
    f = open(path)
    json_file = json.load(f)

    return json_file
