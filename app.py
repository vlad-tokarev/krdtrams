from datetime import datetime
from time import sleep

import requests

import conf


def get_timestamp():
    return int(datetime.utcnow().timestamp() * 1000)


def save(data):
    raise NotImplementedError


def fetch():

    current_timestamp = get_timestamp()

    resp = requests.get(f'{conf.TRAM_API_DOMAIN}/krasnodar/gps.txt?{current_timestamp}')

    if resp.status_code == 200:
        return resp.content
    else:
        raise NotImplementedError


def run():
    while True:
        data = fetch()
        save(data)
        sleep(conf.FETCH_PERIOD)


if __name__ == '__main__':

    run()
