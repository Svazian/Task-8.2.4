import json

import requests

from config import KEYS


class CountArguments(Exception):
    pass


class CompareCurrencies(Exception):
    pass


class APIWorker:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise CompareCurrencies(f'ERROR: Введены одинаковые валюты {base}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={KEYS[quote]}&tsyms={KEYS[base]}')

        return float(json.loads(r.content)[KEYS[base]]) * float(amount)