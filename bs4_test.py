from bs4 import BeautifulSoup
import csv
import requests
import pandas as pd

def web_scraping_b4():
    URL = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

    r = requests.get(URL, headers=headers)
    
    html_content = r.text
    soup = BeautifulSoup(html_content, 'html.parser')

    product_list = [] # a list to store products
   
    table = soup.find('div', attrs = {'class':'col-md-9'}) 
    table_new = table.find('div', attrs = {'class':"row"})
    rows = table_new.find_all('div', attrs = {'class':"caption"})

    print(rows)

    print("-------------------------------------")
    filename = 'products.csv'
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f,['item','price'])
        w.writeheader()
        for row in rows:
            products={}  
            products['item'] = row.a['title']
            # print(item)
            products['price'] = row.find('h4', class_ = 'pull-right price').text ##hotel.find('a', class_ = 'review_count').text
            # print(price)
            product_list.append(products)
            w.writerow(products)
    
    print(product_list)

web_scraping_b4()
