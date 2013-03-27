import urllib2, json, pprint
from collections import defaultdict
from random import choice

#TODO: Organize these into function calls

toppingType = ['Cheese', 'Dough', 'Meats', 'Veggies']

# get json from scraper
req  = urllib2.Request("https://api.scraperwiki.com/api/1.0/datastore/sqlite?format=jsondict&name=pizza_topping_scraper&query=select%20*%20from%20%60pizzas%60%20order%20by%20'toppingType'")
r = urllib2.urlopen(req)
jsonResponse = json.loads(r.read())

# collapse json object to dictionary
all = defaultdict(list)
for i in jsonResponse :
	all[i['toppingType']].append(i['topping'])

# Generate pizza, default to one topping per catagory
def getRandomPizza(Cheese=1, Dough=1, Meats=1, Veggies=1):
	arg = locals()
	myPizza = defaultdict(list)
	for topping in toppingType: # TODO: check for duplicates
		for n in range(arg.get(topping)):
			myPizza[topping].append(choice(all[topping]))
	return myPizza

# Example
megapizza = getRandomPizza(4,1,6,2)
# print megapizza.items()
# print "Ordered pizza with meats: " + ', '.join([n for n in megapizza["Meats"]])