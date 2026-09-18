# toan_hoc.py

def cong(a, b):
    return a + b

def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

PI = 3.14159