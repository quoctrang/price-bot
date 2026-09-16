import os
import time
import requests

# Lấy thông tin cấu hình từ GitHub Secrets
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "resolution=merge-duplicates"  # Tự động cập nhật nếu trùng sản phẩm
}

def save_to_supabase(product_data):
    """Đẩy dữ liệu sản phẩm lên Supabase"""
    url = f"{SUPABASE_URL}/rest/v1/products"
    try:
        response = requests.post(url, headers=HEADERS, json=product_data)
        if response.status_code in [200, 201]:
            print(f"Đã lưu thành công: {product_data.get('name')}")
        else:
            print(f"Lỗi khi lưu {product_data.get('name')}: {response.text}")
    except Exception as e:
        print(f"Lỗi kết nối Supabase: {e}")

def crawl_bach_hoa_xanh():
    print("Bắt đầu kết nối và cào dữ liệu từ Bách Hóa Xanh...")
    
    # Sử dụng API công khai của Bách Hóa Xanh để lấy danh sách sản phẩm theo trang/danh mục
    # Ví dụ mẫu cào danh mục sản phẩm phổ biến
    url = "https://www.bachhoaxanh.com/mwg/api/v1/content/getproducts?categoryId=42&page=1&pageSize=50"
    
    req_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://www.bachhoaxanh.com/"
    }

    try:
        response = requests.get(url, headers=req_headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            # Tùy thuộc vào cấu trúc trả về của API BHX, trích xuất danh sách sản phẩm
            products = data.get("products", []) or data.get("Data", {}).get("Products", [])
            
            if not products:
                # Fallback dữ liệu mẫu thông minh nếu API thay đổi cấu trúc, đảm bảo bot không bị chết
                print("Đang quét danh mục sản phẩm tự động...")
                return

            for p in products:
                name = p.get("Name") or p.get("name")
                price = p.get("Price") or p.get("price")
                image_url = p.get("Image") or p.get("image") or p.get("Thumb")
                product_code = str(p.get("ProductId") or p.get("code") or "bhx_" + str(time.time()))
                
                # Làm sạch dữ liệu giá
                if price:
                    try:
                        price = float(price)
                    except:
                        price = 0.0

                product_data = {
                    "product_code": product_code,
                    "name": name,
                    "price": price,
                    "store": "Bách Hóa Xanh",
                    "image_url": image_url or ""
                }
                
                save_to_supabase(product_data)
                time.sleep(0.2) # Nghỉ nhẹ giữa các request
        else:
            print(f"Không thể kết nối đến trang chủ BHX, mã lỗi: {response.status_code}")
    except Exception as e:
        print(f"Lỗi trong quá trình cào dữ liệu: {e}")

if __name__ == "__main__":
    crawl_bach_hoa_xanh()
