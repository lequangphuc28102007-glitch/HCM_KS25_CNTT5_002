inventory = []

def status_item(item_stock, item_at_least_stock):
    item_stock = int(item_stock)
    item_at_least_stock = int(item_at_least_stock)

    if item_stock == 0:
        inventory[0]["status"] = 'hết hàng'
    elif item_stock < item_at_least_stock:
        inventory[0]["status"] =  'cảnh báo'
    elif item_stock > item_at_least_stock * 3:
        inventory[0]["status"] = 'an toàn'
    else:
        inventory[0]["status"] = 'quá tải'

def calculate_inventory(item_stock, item_price):
    item_stock = int(item_stock)
    item_price = int(item_price)
    return item_stock * item_price

def display_inventory():

    print("=== DANH SÁCH KHO HÀNG ===")


    print(f"{"ID":<20}{"tên sản phẩm":<20}{"đơn giá":<20}{"tồn kho":<20}{"tồn kho tối thiểu":<20}{"tổng giá tiền kho hàng":<20}{"trạng thái":<20}")
    for item in inventory:
        print(
            f"{item['id']:<10} | {item['name']:<20} | {item['price']:<20} | {item['stock']:<20} | {item['at_least_stock']:<20} | {item['total_stock']:<20} | {item['status']:<20}")

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

def statistic():
    count_status_empty = 0
    count_status_warning = 0
    count_status_safe = 0
    count_status_over = 0


    for item in inventory:
        if item['status'] == "cảnh báo":
            count_status_warning += 1
        elif item['status'] == "hết hàng":
            count_status_empty += 1
        elif item['status'] == "an toàn":
            count_status_safe += 1
        else:
            count_status_over += 1

    print(f"{"an toàn:"}{count_status_safe}\n"
        f"{"hết hàng:"}{count_status_empty}\n"
        f"{"cảnh báo:"}{count_status_warning}\n"
        f"{"quá tải:"}{count_status_over}" )
    
def find_item():
    keyword = input("hãy nhập vào mã sản phẩm hoặc tên sản phẩm cần tìm:").strip()
    found = False
    for item in inventory:
        if item['id'].lower() == keyword.lower() or item['name'].lower().split() == keyword.lower():

            print("=== sản phẩm cần tìm === ")

            print(f"{"ID":<20}{"tên sản phẩm":<20}{"đơn giá":<20}{"tồn kho":<20}{"tồn kho tối thiểu":<20}{"tổng giá tiền kho hàng":<20}{"trạng thái":<20}")
            print(f"{item['id']:<10} | {item['name']:<20} | {item['price']:<20} | {item['stock']:<20} | {item['at_least_stock']:<20} | {item['total_stock']:<20} | {item['status']:<20}")

def main():
    while True:
        print("=== QUẢN LÍ KHO ===")
        print("1.hiển thị danh sách kho hàng")
        print("2.khai báo sản phẩm mới")
        print("3.cập nhật số lượng và giá vốn")
        print("4.xóa sản phẩm khỏi danh mục")
        print("5.tìm kiếm sản phẩm")
        print("6.thống kê trạng thái kho hàng")
        print("7.thoát chương trình")

        choice = input("hãy nhập vào lựa chọn")


        match choice:
            case "1":
                display_inventory()
            case "2":
                add_inventory()
            case "3":
                update_inventory()
            case "4":
                remove_inventory()
            case "5":
                find_item()
            case "6":
                statistic()
            case "7":
                print("đã thoát chương trình")
                break
            case _:
                print("lựa chọn không hợp lệ")
                continue
main()