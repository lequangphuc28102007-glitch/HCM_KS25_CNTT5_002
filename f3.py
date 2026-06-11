inventory = [{
    "id": "SP001",
    "name": "chuot khong day Logitech",
    "price": 250000,
    "stock": 15,
    "at_least_stock": 20,
    "total_stock": 3750000,
    "status": "cảnh báo"}
]

def status_item(item_stock, item_at_least_stock):
    if item_stock == 0:
        inventory["status"] = "hết hàng"
    elif item_stock < item_at_least_stock:
        inventory["status"] =  "cảnh báo"
    elif item_stock > item_at_least_stock * 3:
        inventory["status"] = "an toàn"
    else:
        inventory["status"] = "quá tải"

def calculate_inventory(item_stock, item_price):
    item_stock = int(item_stock)
    item_price = int(item_price)
    return item_stock * item_price

def update_inventory():

    item_id = input("hãy nhập vào mã sản phẩm cần tìm:")
    found = False
    for item in inventory:
        if item['id'].lower() == item_id.lower():

            new_price = input("hãy nhập vào đơn giá mới:")
            new_stock = input("hãy nhập vào số lượng mới:")
            new_at_least_stock = input("hãy nhập vào định mức mới:")

            new_status = status_item(new_stock, new_at_least_stock)
            new_total = calculate_inventory(new_stock, new_price)

            item['price'] = new_price
            item['stock'] = new_stock
            item['at_least_stock'] = new_at_least_stock
            item['status'] = new_status
            item['total_stock'] = new_total

            found = True
            break
        if not found:
            print("không tìm thấy")
            continue
        
update_inventory()
        




