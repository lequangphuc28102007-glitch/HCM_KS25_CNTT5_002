inventory = [{
    "id": "SP001",
    "name": "chuot khong day Logitech",
    "price": 250000,
    "stock": 15,
    "at_least_stock": 20,
    "total_stock": 3750000,
    "status": "cảnh báo"}
]

def remove_inventory():
    item_id = input("hãy nhập vào mã sản phẩm cần tìm:")
    found = False
    for item in inventory:
        if item['id'].lower() == item_id.lower():

            answer = input("bạn có chắc muốn xóa (y-n):")
            if answer.lower() == "y":
                inventory.remove()
                print("đã xóa thành công")
                found = True
                break
            else:
                print("đã hủy thao tác")
                break

remove_inventory()

