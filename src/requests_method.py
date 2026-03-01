import requests
import json
import pandas as pd
from bs4 import BeautifulSoup

# Read products_id csv file
df = pd.read_csv("products-0-200000.csv")  #

headers = {"User-Agent": "Mozilla/5.0"}
products = []

success_count = 0
error_count = 0

# Open log file to write messages
log_file = open("log.txt", "w", encoding="utf-8")

for product_id in df["id"]:
    url = f"https://api.tiki.vn/product-detail/api/v1/products/{product_id}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
        except json.JSONDecodeError:
            msg = f"[ERROR] Can not parse JSON for product {product_id}\n"
            print(msg.strip())
            log_file.write(msg)
            error_count += 1
            continue

        # html description -> clean text
        raw_description = data.get("description", "")
        soup = BeautifulSoup(raw_description, "html.parser")
        clean_description = soup.get_text(separator=" ", strip=True)

        product_info = {
            "id": data.get("id"),
            "name": data.get("name"),
            "url_key": data.get("url_key"),
            "price": data.get("price"),
            "description": clean_description,
            "images": [img.get("base_url") for img in data.get("images", [])]
        }

        products.append(product_info)
        success_count += 1
        msg = f"[OK] GET JSON successfully for product {product_id}\n"
        print(msg.strip())
        log_file.write(msg)
    else:
        msg = f"[ERROR] Failed {response.status_code} to GET product {product_id}\n"
        print(msg.strip())
        log_file.write(msg)
        error_count += 1

# Save with "data": array of products
output = {"data": products}

with open("products_full.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=4)

# Summary
summary = (
    f"=== Result ===\n"
    f"Numbers of product GET succesfully: {success_count}\n"
    f"Numbers of ERROR GET: {error_count}\n"
    f"Saved to products_full.json\n"
)
print(summary.strip())
log_file.write(summary)

log_file.close()
