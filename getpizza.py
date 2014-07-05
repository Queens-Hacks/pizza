import requests
from bs4 import BeautifulSoup
from random import randrange

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

def pickToppings(meat, vege, sauce, cheese):
    number_of_toppings = [meat, vege, sauce, cheese]
    toppings_lists = getToppings()
    toppings_chosen = []

    for t in range(4):
        for i in range(number_of_toppings[t]):
            random_num = randrange(len(toppings_lists[t]))
            toppings_chosen.append(toppings_lists[t].pop(random_num))
    return toppings_chosen

if __name__ == '__main__':
    pizza = pickToppings(1, 1, 1, 1)
    print(pizza)
