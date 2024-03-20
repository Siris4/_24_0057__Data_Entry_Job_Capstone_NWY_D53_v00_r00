from bs4 import BeautifulSoup
import requests
import pprint

# CONSTANTS:
# LIMIT_OF_MAXIMUM_ARTICLES_TO_DATA_SCRAPE = 32

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser')

# printes out in a formatted version of the page source data in the website:
pprint.pprint(soup)

