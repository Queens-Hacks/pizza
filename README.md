# Random Pizza-Pizza Generator

    Generates a random listing of toppings for a Pizza-Pizza

## Usage

The Pizza-Pizza generator is avaliable online at [http://qhack.ca/pizza](http://qhack.ca/pizza). 

If you want to run it yourself, you can start a local python server by running

```bash
python -m SimpleHTTPServer
```

And can then access the Pizza Generator at [https://localhost:8000](https://localhost:8000).

## Scraping

The topping information is scraped from Pizza-Pizza's website. You can scrape it by using the Python program in `scraper/`.

```bash
cd scraper                      # Enter the scraper directory
virtualenv env                  # Create a Virtualenv
. env/bin/activate              # Activate the Virtualenv
pip install -r requirements.txt # Install the required packages
python getpizza.py              # Run the getpizza program
```

