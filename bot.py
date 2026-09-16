import requests
from datetime import datetime

SUPABASE_URL = "https://nizpwabxszlsscbewtro.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5penB3YWJ4c3psc3NjYmV3dHJvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODk1MzMzODYsImV4cCI6MjEwNTEwOTM4Nn0.Ej7cw2jGIg7-PHg_FRHmP63zgEX0P7BO5DaJVNjrC8Y"

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}

def upsert_product(product_code, name, store, price):
    data = {
        "product_code": product_code,
        "name": name,
        "store": store,
        "price": price,
        "updated_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    url = f"{SUPABASE_URL}/rest/v1/products"
    response = requests.post(url, headers=headers, json=data)
    if response.status_code in [200, 201]:
        print(f"Đã cập nhật: {name} tại {store} giá {price}đ")
    else:
        print(f"Lỗi: {response.text}")

if __name__ == "__main__":
    # Cập nhật thử một vài sản phẩm mẫu vào kho
    upsert_product("PROBI_5", "Sữa chua uống Probi lốc 5", "Bách Hoá Xanh", 22200)
    upsert_product("PROBI_5", "Sữa chua uống Probi lốc 5", "Shopee", 20500)
    upsert_product("PROBI_5", "Sữa chua uống Probi lốc 5", "WinMart", 20500)
    upsert_product("Redbull 250", "Nước uống tăng lực Việt Redbull lon 250ml", "Bách Hoá Xanh", 11600)
    upsert_product("Redbull 250", "Nước uống tăng lực Việt Redbull lon 250ml", "Shopee", 16000)
    upsert_product("Redbull 250", "Nước uống tăng lực Việt Redbull lon 250ml", "WinMart", 12800)
    upsert_product("STING_330", "Nước tăng lực Sting hương dâu 330ml", "Bách Hoá Xanh", 11500)
    upsert_product("STING_330", "Nước tăng lực Sting hương dâu 330ml", "Shopee", 18000)
    upsert_product("STING_330", "Nước tăng lực Sting hương dâu 330ml", "WinMart", 12200)
    upsert_product("NSPN 1kg2", "Ngôi sao Phương Nam xanh lá 1.284kg", "Bách Hoá Xanh", 71500)
    upsert_product("NSPN 1kg2", "Ngôi sao Phương Nam xanh lá 1.284kg", "Shopee", 82000)
    upsert_product("NSPN 1kg2", "Ngôi sao Phương Nam xanh lá 1.284kg", "WinMart", 74900)
