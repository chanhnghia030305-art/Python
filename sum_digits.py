def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10   # lấy chữ số cuối cùng, cộng vào tổng
        n = n // 10        # bỏ chữ số cuối, dùng chia nguyên
    print(total)

sum_digits(1234)