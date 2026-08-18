num1 = float(input("Nhập số thứ nhất: "))
operator = input("Nhập phép toán (+, -, *, /): ")
num2 = float(input("Nhập số thứ hai: "))

if (operator == "+"):
    result = num1 + num2
    print(f"Kết quả: {result}")
elif (operator == "-"):
    result = num1 - num2
    print(f"Kết quả: {result}")
elif (operator == "*"):
    result = num1 * num2
    print(f"Kết quả: {result}")
elif (operator == "/"):
    if num2 != 0:
        result = num1 / num2
        print(f"Kết quả: {result}")
    else:
        print("Lỗi: Số thứ hai không thể là 0")
else:
    print("Lỗi: Phép toán không hợp lệ")