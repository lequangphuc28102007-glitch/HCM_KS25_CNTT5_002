inventory = []


def display_inventory():

    print("=== DANH SÁCH KHO HÀNG ===")


    print(f"{"ID":<20}{"tên sản phẩm":<20}{"đơn giá":<20}{"tồn kho":<20}{"tồn kho tối thiểu":<20}{"tổng giá tiền kho hàng":<20}{"trạng thái":<20}")
    for item in inventory:
        print(
            f"{item['id']:<10} | {item['name']:<20} | {item['price']:<20} | {item['stock']:<20} | {item['at_least_stock']:<20} | {item['total_stock']:<20} | {item['status']:<20}")

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
                
            case "3":

            case "4":

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