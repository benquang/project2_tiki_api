# Get API Project2

Both requests and aiohttp packages are using for creating product JSON files. Scripts in `/src` and results in `/results` folder.

## I. Install packages

Get into python environment (activate), open CMD and using pip:

- pip install requests
- pip install aiohttp
- pip install bs4

## II. Example of a batch of JSON product list file:
```swift
{
  "data": [{object 1}, {object 2},... {object n}]
}
```

![Demo](assets/JSON_structure.png)

Back to Notion: https://www.notion.so/Project-2-30fdcb66205b80d3a523d99b8ea08b45?source=copy_link


# GET API Tiki App PJ

## Overview
A Python application for fetching data from Tiki API using asynchronous requests.

## Project Structure
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

## Requirements
- Python 3.8+
- `aiohttp` - Asynchronous HTTP client
- `requests` - HTTP library
- `bs4` (BeautifulSoup) - HTML and XML parsing
- 
## Installation
```bash
pip install aiohttp requests bs4
```

## Usage
Run the .py file for each method using for fetching Tiki product data (aiohttp & requests):
```bash
python src/aiohttp_method.py
```

## Output
Results are saved as JSON data in the `results/json_products` folder:
```json
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
        }
```

## Features
- Asynchronous API requests
- JSON data export
- Error handling and logging
