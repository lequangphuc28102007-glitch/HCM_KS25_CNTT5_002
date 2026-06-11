inventory = [{
    "id": "SP001",
    "name": "chuot khong day Logitech",
    "price": 250000,
    "stock": 15,
    "at_least_stock": 20,
    "total_stock": 3750000,
    "status": "cảnh báo"}
]

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
        f"{"quá tải:"}{count_status_over}"  
        )
    
statistic()