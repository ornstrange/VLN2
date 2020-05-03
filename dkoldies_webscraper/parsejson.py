import os
import json
import base64
import requests

names = {}

def b64urlimgid(name, len_):
    return base64.urlsafe_b64encode(name.encode()).decode()[:len_]

def urltoimg(name, url):
    len_ = 4
    id_ = b64urlimgid(name, len_)
    while id_ in names:
        len_ += 1
        id_ = b64urlimgid(name, len_)
        if "=" in id_:
            raise Exception
    names[id_] = 1
    img_data = requests.get(url).content
    with open(f"img/products/{id_}.jpg", "wb") as f:
        f.write(img_data)
    return id_

products = []
prod_jsons = list(filter(lambda x: ".json" in x, os.listdir('.')))
for fname in prod_jsons:
    with open(fname, "r") as f:
        pj = json.load(f)
        if products:
            products += pj
        else:
            products = pj

for i, product in enumerate(products):
    # price to int, Capitalize name, download img/s create folders
    product['name'] = product['name'].title()
    product['price'] = int(float(product['price']) * 103)
    ids = []
    for img_url in product['imgs']:
        img_url = img_url.strip()
        ids.append(urltoimg(product['name'], img_url))
    product['imgs'] = ";".join(ids)
    print(f"{i+1}/{len(products)}: {product['name']}, {product['price']}, {product['imgs']}")

with open("products.json", "w") as f:
    json.dump(products, f, indent=4)

