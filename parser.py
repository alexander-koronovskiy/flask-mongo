import json

import lxml
import requests
from bs4 import BeautifulSoup


def parse_page(url: str) -> lxml:
    response = requests.get(url)
    return BeautifulSoup(response.text, "lxml")


def get_exchange_rate(url: str) -> json:
    return requests.get(url).json()


# план работ
# 1 поиск ресурса\ ресурсов для получения курса валют с помощью ф-ии get_exchange_rate
# 2 запись в БД ВСЕХ найденных курсов
# 3 пробная ф-ия для принта выбранного курса из БД
