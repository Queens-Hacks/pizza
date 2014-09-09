#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
from random import randrange
import json


def parse_toppings(html):
    soup = BeautifulSoup(html)

    choices = []

    for tag in soup.find_all('h3'):
        choices.append(tag.get_text())

    for i in range(0, len(choices)):
        choices[i] = choices[i].replace('\n', '').replace('\r', '').rstrip().lstrip()
    choices.pop()
    choices.pop(0)

    return choices


def split_sauces_dough(toppings):
    sauces = []
    doughs = []
    for topping in toppings:
        if 'Sauce' in topping:
            sauces.append(topping)
        elif 'Dough' in topping:
            doughs.append(topping)
        else:
            raise ValueError('Topping not a sauce or dough? {}'.format(topping))
    return sauces, doughs


def get_toppings():
    toppings_lists = []

    r = requests.get("http://www.pizzapizza.ca/fresh-toppings-bk/meattab/")
    toppings_lists.append(parse_toppings(r.text))

    r = requests.get("http://www.pizzapizza.ca/fresh-toppings-bk/veggietab/")
    toppings_lists.append(parse_toppings(r.text))

    r = requests.get("http://www.pizzapizza.ca/fresh-toppings-bk/saucesanddoughtab/")
    toppings_lists.extend(split_sauces_dough(parse_toppings(r.text)))

    r = requests.get("http://www.pizzapizza.ca/fresh-toppings-bk/cheesetab/")
    toppings_lists.append(parse_toppings(r.text))

    return toppings_lists


if __name__ == '__main__':
    toppings = get_toppings()
    with open('toppings.json', 'w') as f:
        json.dump(toppings, f, indent=4)
