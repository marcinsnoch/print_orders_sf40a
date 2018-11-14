#!/usr/bin/python

import config
import time
import requests


def main():
    r = requests.get(config.SERVER_API['host'] + 'orders', params={'token': config.SERVER_API['token']})

    data = r.json()

    orders = []

    while True:
        i = 1
        for order in data:
            if order['order_no'] not in orders:
                orders.append(order['order_no'])
                print(i, "New order: ", order['order_no'].encode())
                i = i + 1
        print('Waiting...')
        time.sleep(3600)


if __name__ == "__main__":
    main()
