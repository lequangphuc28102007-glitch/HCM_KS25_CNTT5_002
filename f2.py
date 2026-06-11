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
    item_stock = int(item_stock)
    item_at_least_stock = int(item_at_least_stock)

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

def add_inventory():

    item_id = input("hãy nhập vào mã đơn:")

    item_name = input("hãy nhập tên sản phẩm:")

    item_price = input("hãy nhập vào giá tiền:")

    item_stock = input("hãy nhập số lượng tồn:")

    item_at_least_stock = input("hãy nhập vào số lượng tồn tối thiểu:")

    total_cost_item = calculate_inventory(item_stock, item_price)

    item_status = status_item(item_stock, item_at_least_stock)

    new_item = {
    "id": item_id,
    "name": item_name,
    "price": item_price,
    "stock": item_stock,
    "at_least_stock": item_at_least_stock,
    "total_stock": total_cost_item,
    "status": item_status
    }

    inventory.append(new_item)

    print("đã thêm thành công")

add_inventory()

