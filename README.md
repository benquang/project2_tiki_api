# GET API Tiki App PJ

## 📖 Overview
A Python application for fetching data from Tiki API using asynchronous requests.

## 📁 Project Structure
```
GET API Tiki App/
├── src/
│   ├── requests_method.py
│   ├── aiohttp_method.py
│   └── statistic.ipynb
├── assets/
│   └── [images, documentation]
├── results/
│   ├── errors_batches/
│   ├── json_products/
│   ├── get_again_error_products/
```

## 📋 Requirements
- Python 3.8+
- `aiohttp` - Asynchronous HTTP client
- `requests` - HTTP library
- `bs4` (BeautifulSoup) - HTML and XML parsing
- 
## 💾 Installation
```bash
pip install aiohttp requests bs4
```

## 🚀 Usage
Run the .py file for each method using for fetching Tiki product data (aiohttp & requests):
```bash
python src/aiohttp_method.py
```

## 📊 Output
   1. Results are saved as JSON data in the `results/json_products` folder:
      ```json
        {
        "data": [
                {
                    "id": 154155413,
                    "name": "",
                    "url_key": "bo-do-choi-tau-hoa-do-choi-xe-lua-co-duong-ray-lap-rap-nhieu-mau-sac-cho-be-p154155413",
                    "price": 59000,
                    "description": "...",
                    "images": [
                        "https://salt.tikicdn.com/ts/product/a6/f2/d0/bb744634f1ed0ae8a3e71bfe35a73c7c.jpg",
                        "https://salt.tikicdn.com/ts/product/f8/cd/15/c342466e4a390ff8c1da6cf43b7ba097.jpg"
                    ]
                }, {}
        ]
        }
      ```

   2. Execution time for each method:
      So we have a 200 STATUS response for getting product successfully, with ~100 products/2 minutes so the estimated execution time is about 66 hours.
      ```
        [OK] GET JSON successfully for product 1391347
        [OK] GET JSON successfully for product 74897599
        [OK] GET JSON successfully for product 154155413
        [OK] GET JSON successfully for product 253117062
      ```

      The exection time for aiohttp + asyncio method is about 90 minutes, this is numbers of ERROR products:
      ```
      Numbers of ERROR products: 9456
      ERROR Catgeory:
      - HTTP 404: 6638
      - HTTP 429: 2810
      - 'NoneType' object is not iterable: 8
      ```
   3. Execution again for 429 & 404 ERROR products and save to CSV list of product ids:
      We retry for list of 429 ERROR products and get more sucessfully products (2698/2810 [OK]). For list of 404 ERROR products (with retry request 5 times and 1 second sleep time), we found that all of them are NOT FOUND product from Tiki API, so from 200000 unique product ids, we get:
       ```
      Total of GET successfully products: 193242 
      Numbers of ERROR products: 6758
      - HTTP 404: 6750
      - 'NoneType' object is not iterable: 8 (the image information is NULL, we can ignore this or check again to get them)
      ```

- 
## ⭐ Features
- Asynchronous API requests
- JSON data export
- Error handling and logging
