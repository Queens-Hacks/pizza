import requests
from bs4 import BeautifulSoup
from random import randrange
import json

def parseToppings(soup):

    choices = []

    for tag in soup.find_all('h3'):
        choices.append(tag.get_text())

    for i in range(0, len(choices)):
        choices[i] = choices[i].replace('\n', '').replace('\r', '').rstrip().lstrip()
    choices.pop()
    choices.pop(0)

    return choices

def getToppings():
    all_soup = []

    r = requests.get("http://www.pizzapizza.ca/fresh-toppings-bk/meattab/")
    all_soup.append(BeautifulSoup(r.text))
    r = requests.get("http://www.pizzapizza.ca/fresh-toppings-bk/veggietab/")
    all_soup.append(BeautifulSoup(r.text))
    r = requests.get("http://www.pizzapizza.ca/fresh-toppings-bk/saucesanddoughtab/")
    all_soup.append(BeautifulSoup(r.text))
    r = requests.get("http://www.pizzapizza.ca/fresh-toppings-bk/cheesetab/")
    all_soup.append(BeautifulSoup(r.text))

    toppings_lists = []

    for soup in all_soup:
        toppings_lists.append(parseToppings(soup))
    return toppings_lists

if __name__ == '__main__':
    with open('toppings.json', 'w') as f:
        f.write(json.dumps(getToppings(), indent=4));
