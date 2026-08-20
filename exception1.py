try:
    num1 = int(input("Nhập vào tử số: "))
    num2 = int(input("Nhập vào mẫu số: "))
    result = num1 / num2
    print(f"Kết quả phép chia là: {result}")
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0. Vui lòng nhập lại mẫu số khác 0.")
except ValueError:
    print("Lỗi: Vui lòng nhập vào một số nguyên hợp lệ.")
except:
    print("Có lỗi xảy ra, vui lòng liên hệ trung tâm hỗ trợ để được giúp đỡ.")