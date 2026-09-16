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
    print("Đang nạp dữ liệu sản phẩm kèm hình ảnh...")
    
    # Danh sách sản phẩm có đầy đủ link ảnh chuẩn
    sample_products = [
        {"product_code": "bhx_01", "name": "Mì Hảo Hảo chua cay thùng 30 gói", "price": 125000, "store": "Bách Hóa Xanh", "image_url": "https://cdn.tgdd.vn/Products/Images/42/86737/bhx/thung-30-goi-mi-hao-hao-chua-cay-75g-202004151441315629.jpg"},
        {"product_code": "bhx_02", "name": "Thùng 24 lon nước ngọt Coca Cola 320ml", "price": 205000, "store": "Bách Hóa Xanh", "image_url": "https://cdn.tgdd.vn/Products/Images/2433/74929/bhx/thung-24-lon-nuoc-giai-khat-coca-cola-320ml-202206221008272996.jpg"},
        {"product_code": "bhx_03", "name": "Sữa tươi tiệt trùng Vinamilk ít đường lốc 4 hộp 180ml", "price": 32000, "store": "Bách Hóa Xanh", "image_url": "https://cdn.tgdd.vn/Products/Images/2386/194451/bhx/loc-4-hop-sua-tuoi-tiet-trung-it-duong-vinamilk-180ml-202303081442116035.jpg"},
        {"product_code": "bhx_04", "name": "Dầu ăn Neptune Light 1L", "price": 58000, "store": "Bách Hóa Xanh", "image_url": "https://cdn.tgdd.vn/Products/Images/2455/229983/bhx/dau-an-cao-cap-neptune-light-chai-1-lit-202009211607593259.jpg"},
        {"product_code": "bhx_05", "name": "Nước giặt OMO Matic đậm đặc cửa trên 3.1kg", "price": 165000, "store": "Bách Hóa Xanh", "image_url": "https://cdn.tgdd.vn/Products/Images/2464/228198/bhx/tu-nhua-dung-do-da-nang-dai-loan-202009081512411234.jpg"}
    ]

    for p in sample_products:
        save_to_supabase(p)
        time.sleep(0.2)
    print("Đã nạp xong toàn bộ sản phẩm kèm ảnh!")

if __name__ == "__main__":
    sync_products()
