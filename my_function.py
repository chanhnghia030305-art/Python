from math import *
def prime_number(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True 

for num in range(1, 41):
    if prime_number(num):
        print(num, end=' ')



 
        