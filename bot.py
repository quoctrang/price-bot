import os
import time
import requests

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "resolution=merge-duplicates"
}

def sync_products():
    print("Đang cập nhật danh sách sản phẩm từ các siêu thị và cửa hàng tiện lợi...")
    
    sample_products = [
        # --- Sản phẩm tại Bách Hóa Xanh ---
        {
            "product_code": "bhx_01", 
            "name": "Mì Hảo Hảo chua cay thùng 30 gói", 
            "price": 125000, 
            "store": "Bách Hóa Xanh", 
            "image_url": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=150&auto=format&fit=crop&q=80"
        },
        {
            "product_code": "bhx_02", 
            "name": "Thùng 24 lon nước ngọt Coca Cola 320ml", 
            "price": 205000, 
            "store": "Bách Hóa Xanh", 
            "image_url": "https://images.unsplash.com/photo-1554866585-cd94860890b7?w=150&auto=format&fit=crop&q=80"
        },

        # --- Sản phẩm tương tự tại Circle K ---
        {
            "product_code": "ck_02", 
            "name": "Thùng 24 lon nước ngọt Coca Cola 320ml", 
            "price": 220000, 
            "store": "Circle K", 
            "image_url": "https://images.unsplash.com/photo-1554866585-cd94860890b7?w=150&auto=format&fit=crop&q=80"
        },

        # --- Sản phẩm tại FamilyMart ---
        {
            "product_code": "fm_02", 
            "name": "Thùng 24 lon nước ngọt Coca Cola 320ml", 
            "price": 215000, 
            "store": "FamilyMart", 
            "image_url": "https://images.unsplash.com/photo-1554866585-cd94860890b7?w=150&auto=format&fit=crop&q=80"
        },

        # --- Sản phẩm tại 7-Eleven ---
        {
            "product_code": "sev_01", 
            "name": "Mì Hảo Hảo chua cay thùng 30 gói", 
            "price": 130000, 
            "store": "7-Eleven", 
            "image_url": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=150&auto=format&fit=crop&q=80"
        },

        # --- Sản phẩm tại Ministop ---
        {
            "product_code": "ms_01", 
            "name": "Mì Hảo Hảo chua cay thùng 30 gói", 
            "price": 128000, 
            "store": "Ministop", 
            "image_url": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=150&auto=format&fit=crop&q=80"
        }
    ]

    url = f"{SUPABASE_URL}/rest/v1/products"
    for p in sample_products:
        try:
            response = requests.post(url, headers=HEADERS, json=p)
            if response.status_code in [200, 201]:
                print(f"Đã lưu: {p['name']} tại {p['store']}")
            else:
                print(f"Lỗi: {response.text}")
        except Exception as e:
            print(f"Lỗi kết nối: {e}")
        time.sleep(0.1)

    print("Hoàn tất cập nhật dữ liệu các cửa hàng tiện lợi!")

if __name__ == "__main__":
    sync_products()
