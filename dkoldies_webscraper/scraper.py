import requests
from bs4 import BeautifulSoup
import json

## all prods
with open("gameboy-games.html", "r") as f:
    content = ""
    for l in f.readlines():
        content += l
soup = BeautifulSoup(content, 'html.parser')
prods = soup.find_all('figure', class_="card-figure")
ls = []
for prod in prods:
    ls.append("https://" + prod.a['href'][2:-1])

## items
items = []

for g in ls:
    try:
        ## single item
        page = requests.get(g)
        content = page.content
        soup = BeautifulSoup(content, 'html.parser')
        # name
        name = soup.find('h1', class_='productView-title').text.strip()
        # images
        img_links = soup.find_all('a', class_='productView-thumbnail-link')
        img_links = list(map(lambda x: x['href'], img_links))
        # desc
        desc_raw = soup.find('div', class_='product_description')
        if desc_raw.find('p'):
            desc = soup.find('div', class_='product_description').p.text.strip()
        else:
            desc_raw.h2.decompose()
            desc = desc_raw.text.strip()
        # price
        price = soup.find('span', class_='price--rrp').text.strip().replace("$", "")
        if not price:
            price = soup.find('span', class_='price--withoutTax').text.strip().replace("$", "")
        # condition
        cond = soup.find('dd', class_='productView-info-value').text.strip()
        # keywords
        prod_detail = soup.find('article', class_='productView-description').div.div.nextSibling.nextSibling.find_all('dd')
        keywords = ", ".join(map(lambda x: x.text, prod_detail[1:4]))
        # category
        category = prod_detail[2].text
        items.append({
            'name': name,
            'imgs': img_links,
            'desc': desc,
            'price': price,
            'cond': cond,
            'keys': keywords,
            'cat': category
        })
        print("added", g)
    except Exception as err:
        print("failed", g, err)
        pass

with open('gameboy-games.json', 'w+') as ofile:
    json.dump(items, ofile, indent=4)

