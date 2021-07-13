import json

import requests


def get_exchange_rate(url: str, keyword: str) -> json:
    return requests.get(url).json()[keyword]


# план работ

# 0 другие ресурсы для получения курса валют ???

# 1 работа с БД \ запись в БД ВСЕХ полученных курсов
# 2 пробная ф-ия для принта выбранного курса из БД
