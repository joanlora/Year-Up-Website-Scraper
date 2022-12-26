import requests
from bs4 import BeautifulSoup
 
yuny = requests.get('https://www.yearup.org/')
 
print("Programmer: Joan Jose Lora")
print(yuny)
 
# Parsing the HTML
scrape = BeautifulSoup(yuny.content, 'html.parser')

print(scrape.title)
print(scrape.html.name)
print(scrape.input)
print(scrape.link)

print("\n")

scrapeClass = scrape.find('html')
scrapeP = scrapeClass.find_all('p') # finds all paragraph tags

print(scrapeP)



