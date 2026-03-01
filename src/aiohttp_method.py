import aiohttp
import asyncio
import pandas as pd
from bs4 import BeautifulSoup
import json
import logging
import os

# Create folders for results and errors
os.makedirs("result_200k", exist_ok=True)
os.makedirs("error_200k", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="log-20k.txt",
    level=logging.INFO,
    format="%(message)s",
    encoding="utf-8"
)

semaphore = asyncio.Semaphore(40)  #

async def fetch(session, url, idx, product_id):
    async with semaphore:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    try:
                        data = await response.json()
                    except Exception:
                        msg = f"[ERROR] index={idx}, id={product_id}, error=Can not parse JSON"
                        print(msg)
                        logging.error(msg)
                        return None, msg

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

                    msg = f"[OK] index={idx}, id={product_id}"
                    print(msg)
                    logging.info(msg)
                    return product_info, None
                else:
                    msg = f"[ERROR] index={idx}, id={product_id}, error=HTTP {response.status}"
                    print(msg)
                    logging.error(msg)
                    return None, msg
        except Exception as e:
            msg = f"[ERROR] index={idx}, id={product_id}, error={str(e)}"
            print(msg)
            logging.error(msg)
            return None, msg

async def process_batch(batch_df, batch_index):
    products = []
    error_msgs = []

    async with aiohttp.ClientSession(headers={"User-Agent": "Mozilla/5.0"}) as session:
        tasks = []
        for idx, product_id in enumerate(batch_df["id"]):
            url = f"https://api.tiki.vn/product-detail/api/v1/products/{product_id}"
            tasks.append(fetch(session, url, idx + batch_index * len(batch_df), product_id))

        results = await asyncio.gather(*tasks)

    for result, err in results:
        if result:
            products.append(result)
        if err:
            error_msgs.append(err)

    # Save batch result json file
    with open(f"result_200k/product_batch_{batch_index+1}.json", "w", encoding="utf-8") as f:
        json.dump({"data": products}, f, ensure_ascii=False, indent=4)

    # Save batch error file
    with open(f"error_200k/errors_batch_{batch_index+1}.txt", "w", encoding="utf-8") as f:
        for msg in error_msgs:
            f.write(msg + "\n")

    summary = (
        f"=== Batch {batch_index+1} ===\n"
        f"Numbers of products GET successfully: {len(products)}\n"
        f"Numbers of ERROR: {len(error_msgs)}\n"
        f"Saved to result_200k/product_batch_{batch_index+1}.json\n"
        f"Saved to error_200k/errors_batch_{batch_index+1}.txt\n"
    )
    print(summary)
    logging.info(summary)

async def main():
    df = pd.read_csv("products-0-200000.csv")
    batch_size = 1000
    num_batches = (len(df) + batch_size - 1) // batch_size

    for batch_index in range(num_batches):
        start = batch_index * batch_size
        end = min((batch_index + 1) * batch_size, len(df))
        batch_df = df.iloc[start:end]

        print(f"=== Processing batch {batch_index+1}/{num_batches}, including {len(batch_df)} products ===")
        await process_batch(batch_df, batch_index)

if __name__ == "__main__":
    asyncio.run(main())
