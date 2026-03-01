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


# 📦 Tiki API Project

## Giới thiệu
Dự án này được xây dựng nhằm **lấy dữ liệu từ API Tiki** bằng cách sử dụng:
- [aiohttp](https://docs.aiohttp.org/) cho các request bất đồng bộ.
- [requests](https://docs.python-requests.org/) cho các request đồng bộ.
- Jupyter Notebook để phân tích và thử nghiệm.
- Kết quả được lưu dưới dạng **JSON** trong thư mục `results`.

## 📂 Cấu trúc thư mục
├── src/          # Mã nguồn chính (Python scripts)
├── assets/       # Hình ảnh, tài liệu minh họa
├── results/      # Kết quả JSON sau khi gọi API
├── notebooks/    # Jupyter Notebook scripts
└── README.md     # Tài liệu dự án

## 🚀 Cách chạy
### 1. Cài đặt môi trường
```bash
pip install -r requirements.txt
```
### 1. Chạy script python
```bash
python src/get_tiki_api.py
```

📊 Kết quả
* Các file JSON được lưu trong thư mục results/.
* Có thể dùng Notebook để phân tích dữ liệu (ví dụ: thống kê sản phẩm, giá cả, đánh giá).
