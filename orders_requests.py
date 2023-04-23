import configuration
import requests
import data


def new_order_create(body):
    return requests.post(configuration.URL_SERVICE + configuration.ORDERS_PATH, json=body, headers=data.headers)


def get_order_status(track):
    return requests.get(configuration.URL_SERVICE + configuration.RECEIVE_ORDER + track)
