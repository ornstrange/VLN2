import json

with open("products.json", "r") as f:
    products = json.load(f)

header = "INSERT INTO public.products_product(id, keywords, image, name, description, type, price, condition) VALUES\n"
query = "\t({id}, \"{keys}\", \"{imgs}\", \"{name}\", \"{desc}\", \"{cat}\", {price}, \"{cond}\")"

with open("insert.sql", "w") as f:
    f.write(header)
    for i, prod in enumerate(products, 1):
        f.write(query.format(id=i, **prod))
        if i == len(products):
            f.write(";\n")
        else:
            f.write(",\n")

