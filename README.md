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


# GET API Tiki App

## Overview
A Python application for fetching data from Tiki API using asynchronous requests.

## Project Structure
```
GET API Tiki App/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── api_client.py
│   └── utils.py
├── assets/
│   └── [configuration files, images, documentation]
├── results/
│   └── data.json
└── notebook.ipynb
```

## Requirements
- Python 3.8+
- `aiohttp` - Asynchronous HTTP client
- `requests` - HTTP library
- `jupyter` - For notebook exploration

## Installation
```bash
pip install aiohttp requests jupyter
```

## Usage
Run the Jupyter notebook or execute the main script:
```bash
python src/main.py
```

## Output
Results are saved as JSON data in the `results/` folder:
```json
{
    "products": [],
    "status": "success",
    "timestamp": "2024-01-01T00:00:00Z"
}
```

## Features
- Asynchronous API requests
- JSON data export
- Error handling and logging
