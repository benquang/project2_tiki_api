# GET API Tiki App PJ

## 📖 Overview
A Python application for fetching data from Tiki API using asynchronous requests.

## 📁 Project Structure
```
GET API Tiki App/
├── src/
│   ├── requests_method.py
│   ├── aiohttp_method.py
│   └── statistic_&_run_again.py
├── assets/
│   └── [images, documentation]
├── results/
│   ├── errors_batches/
│   ├── json_products/
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
Results are saved as JSON data in the `results/json_products` folder:
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
** ERROR Category**:
- HTTP 404: 6638
- HTTP 429: 2810
- 'NoneType' object is not iterable: 8
- 
## ⭐ Features
- Asynchronous API requests
- JSON data export
- Error handling and logging
