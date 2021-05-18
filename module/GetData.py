import json
import requests


def getter():
    return requests.get('https://www.hpb.health.gov.lk/api/get-current-statistical')


def dump_json(responds, path):
    if responds.status_code == 200:
        with open(path, 'w') as file:
            json.dump(responds.json(), file, sort_keys=True, indent=4)
    else:
        return responds.status_code
