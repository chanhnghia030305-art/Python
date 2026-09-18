# main.py
from task_plus import Task

danh_sach_task = []

def hien_thi_menu():
    print("\n===== QUẢN LÝ CÔNG VIỆC =====")
    print("1. Thêm task")
    print("2. Xem danh sách")
    print("3. Đánh dấu hoàn thành")
    print("4. Xóa task")
    print("5. Thoát")

def them_task():
    ten = input("Nhập tên task: ")
    danh_sach_task.append(Task(ten))
    print("Đã thêm!")

def xem_danh_sach():
    if not danh_sach_task:
        print("Chưa có task nào.")
        return
    for i, task in enumerate(danh_sach_task):
        print(f"{i+1}. {task}")

def hoan_thanh_task():
    xem_danh_sach()
    try:
        idx = int(input("Chọn số thứ tự task đã xong: ")) - 1
        danh_sach_task[idx].danh_dau_hoan_thanh()
        print("Đã cập nhật!")
    except (ValueError, IndexError):
        print("Lựa chọn không hợp lệ.")

def xoa_task():
    xem_danh_sach()
    try:
        idx = int(input("Chọn số thứ tự task cần xóa: ")) - 1
        danh_sach_task.pop(idx)
        print("Đã xóa!")
    except (ValueError, IndexError):
        print("Lựa chọn không hợp lệ.")

def main():
    while True:
        hien_thi_menu()
        lua_chon = input("Chọn chức năng: ")

        if lua_chon == "1":
            them_task()
        elif lua_chon == "2":
            xem_danh_sach()
        elif lua_chon == "3":
            hoan_thanh_task()
        elif lua_chon == "4":
            xoa_task()
        elif lua_chon == "5":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, thử lại.")

if __name__ == "__main__":
    main()