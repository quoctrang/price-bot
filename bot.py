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

def crawl_bach_hoa_xanh():
    print("Bắt đầu kết nối và cào dữ liệu từ Bách Hóa Xanh...")
    
    # URL API danh mục sản phẩm chính thức của Bách Hóa Xanh
    url = "https://www.bachhoaxanh.com/mwg/api/v1/content/getproducts?categoryId=42&page=1&pageSize=20"
    
    # Bộ giả lập trình duyệt chi tiết để vượt tường lửa
    req_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
        "Referer": "https://www.bachhoaxanh.com/",
        "Origin": "https://www.bachhoaxanh.com",
        "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="8", "Google Chrome";v="122"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
    }

    try:
        # Thêm cấu hình Session để giữ kết nối ổn định hơn
        session = requests.Session()
        response = session.get(url, headers=req_headers, timeout=15)
        
        if response.status_code == 200:
            data = response.json()
            products = data.get("products", []) or data.get("Data", {}).get("Products", [])
            
            if not products:
                print("Không tìm thấy sản phẩm trong phản hồi từ API.")
                return

            print(f"Đã tìm thấy {len(products)} sản phẩm. Đang đẩy lên Supabase...")
            for p in products:
                name = p.get("Name") or p.get("name")
                price = p.get("Price") or p.get("price")
                image_url = p.get("Image") or p.get("image") or p.get("Thumb")
                product_code = str(p.get("ProductId") or p.get("code") or "bhx_" + str(time.time()))
                
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
                time.sleep(0.3)
        else:
            print(f"Bách Hóa Xanh từ chối kết nối, mã lỗi: {response.status_code}")
    except Exception as e:
        print(f"Lỗi trong quá trình cào dữ liệu: {e}")

if __name__ == "__main__":
    crawl_bach_hoa_xanh()
