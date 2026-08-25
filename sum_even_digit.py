from math import *
def sum_even_digit(n):
    total = 0
    while n > 0:
        even_digit = n % 10
        if even_digit % 2 == 0:
            total += even_digit
        n = n // 10
    print(total)

def sum_odd_digit(n):
    total = 0
    while n > 0:
        odd_digit = n % 10
        if odd_digit % 2 != 0:
            total += odd_digit
        n = n // 10
    print(total)

def sum_prime_number(n):
    total = 0
    while n > 0:
        prime_number = n % 10
        for i in range(2, isqrt(prime_number) + 1):
            if prime_number % i == 0:
                total += 0
        total += prime_number
        n = n // 10
    print(total)
    
    
def reversed_number(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n = n // 10
    print(rev)
    
def dem_uoc(n):
    """Đếm số lượng ước của n"""
    dem = 0
    for i in range(1, n + 1):
        if n % i == 0:
            dem += 1
    return dem

def kiem_tra_nguyen_to(n):
    """Kiểm tra n có phải số nguyên tố không"""
    if n < 2:
        return False
    return dem_uoc(n) == 2  # chỉ có ước 1 và chính nó


def kiem_tra_nguyen_to(x):
    """Kiểm tra x có phải số nguyên tố không"""
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def in_uoc_nguyen_to(n):
    """In ra các ước của n mà là số nguyên tố"""
    print(f"Các ước nguyên tố của {n} là:", end=" ")
    for i in range(1, n + 1):
        if n % i == 0 and kiem_tra_nguyen_to(i):
            print(i, end=" ")
    print()
    
def uoc_nguyen_to_lon_nhat_toi_uu(n):
    ket_qua = -1
    # Loại bỏ hết thừa số 2
    while n % 2 == 0:
        ket_qua = 2
        n = n // 2
    # Kiểm tra các thừa số lẻ từ 3 trở đi
    i = 3
    while i * i <= n:
        while n % i == 0:
            ket_qua = i
            n = n // i
        i += 2
    # Nếu sau khi chia hết, n còn lại > 2 thì bản thân nó là số nguyên tố lớn nhất
    if n > 2:
        ket_qua = n
    return ket_qua


def kt_so_6(n):
    check = 0
    while n > 0:
        check = n % 10
        if check == 6:
            return 1
        n = n // 10
    return 0  


def n_chia_het_cho_8(n):
    n = abs(n)
    check = 0
    while n > 0:
        check += n % 10
        n = n // 10
    if check % 8 == 0:
        return 1
    return 0


print(n_chia_het_cho_8(2042))
        
        
    





