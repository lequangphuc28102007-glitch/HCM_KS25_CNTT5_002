inventory = [{
    "id": "SP001",
    "name": "chuot khong day Logitech",
    "price": 250000,
    "stock": 15,
    "at_least_stock": 20,
    "total_stock": 3750000,
    "status": "cảnh báo"}
]

def find_item():
    keyword = input("hãy nhập vào mã sản phẩm hoặc tên sản phẩm cần tìm:").strip()
    found = False
    for item in inventory:
        if item['id'].lower() == keyword.lower() or item['name'].lower().split() == keyword.lower():

            print("=== sản phẩm cần tìm === ")

            print(f"{"ID":<20}{"tên sản phẩm":<20}{"đơn giá":<20}{"tồn kho":<20}{"tồn kho tối thiểu":<20}{"tổng giá tiền kho hàng":<20}{"trạng thái":<20}")
            print(f"{item['id']:<10} | {item['name']:<20} | {item['price']:<20} | {item['stock']:<20} | {item['at_least_stock']:<20} | {item['total_stock']:<20} | {item['status']:<20}")
find_item()