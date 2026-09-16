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

def save_to_supabase(product_data):
    url = f"{SUPABASE_URL}/rest/v1/products"
    try:
        response = requests.post(url, headers=HEADERS, json=product_data)
        if response.status_code in [200, 201]:
            print(f"Đã lưu thành công: {product_data.get('name')}")
        else:
            print(f"Lỗi khi lưu {product_data.get('name')}: {response.text}")
    except Exception as e:
        print(f"Lỗi kết nối Supabase: {e}")

def sync_products():
    print("Đang nạp lại dữ liệu sản phẩm kèm link ảnh chuẩn...")
    
    # Sử dụng link hình ảnh minh họa ổn định, sắc nét
    sample_products = [
        {
            "product_code": "bhx_01", 
            "name": "Mì Hảo Hảo chua cay thùng 30 gói", 
            "price": 125000, 
            "store": "Bách Hóa Xanh", 
            "image_url": "https://images.unsplash.com/photo-1612927601601-6638404738ad?w=150&auto=format&fit=crop&q=80"
        },
        {
            "product_code": "bhx_02", 
            "name": "Thùng 24 lon nước ngọt Coca Cola 320ml", 
            "price": 205000, 
            "store": "Bách Hóa Xanh", 
            "image_url": "https://images.unsplash.com/photo-1554866585-cd94860890b7?w=150&auto=format&fit=crop&q=80"
        },
        {
            "product_code": "bhx_03", 
            "name": "Sữa tươi tiệt trùng Vinamilk ít đường lốc 4 hộp 180ml", 
            "price": 32000, 
            "store": "Bách Hóa Xanh", 
            "image_url": "https://images.unsplash.com/photo-1550583724-b2692b85b150?w=150&auto=format&fit=crop&q=80"
        },
        {
            "product_code": "bhx_04", 
            "name": "Dầu ăn Neptune Light 1L", 
            "price": 58000, 
            "store": "Bách Hóa Xanh", 
            "image_url": "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?w=150&auto=format&fit=crop&q=80"
        },
        {
            "product_code": "bhx_05", 
            "name": "Nước giặt OMO Matic đậm đặc cửa trên 3.1kg", 
            "price": 165000, 
            "store": "Bách Hóa Xanh", 
            "image_url": "https://images.unsplash.com/photo-1585421514284-efb74c2b69ba?w=150&auto=format&fit=crop&q=80"
        }
    ]

    for p in sample_products:
        save_to_supabase(p)
        time.sleep(0.2)
    print("Đã hoàn tất nạp lại dữ liệu!")

if __name__ == "__main__":
    sync_products()
