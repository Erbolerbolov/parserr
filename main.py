from bs4 import BeautifulSoup
import requests
from requests import get
import time 
import random


url = 'https://www.kivano.kg/kompyutery?page='
computers = []
count = 1
while count <= 6:
    url = 'https://www.kivano.kg/kompyutery?page=' + str(count)
    print(url)
    response = get(url)
    html_soup = BeautifulSoup(response.text, "html.parser")

    computers_data = html_soup.find_all('div', class_='item product_listbox oh')
    if computers_data != []:
        computers.extend(computers_data)
        value = random.random()
        scaled_value = 1 + (value * (9 - 5))
        print(scaled_value)
        time.sleep(scaled_value)
    else:
        print('empty')
        break
    count += 1

print(len(computers))
print(computers[1])
print()
n = int(len(computers)) - 1
count = 0
while count <= 2:
    info = computers[int(count)]
    price = info.find('div', {'class':'listbox_price text-center'}).text
    title = info.find('div', {'class':'listbox_title oh'}).text
    print(title,' ', price)
    count += 1
        
