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
        



sum_even_digit(2246)
sum_odd_digit(1111)
sum_prime_number(357)