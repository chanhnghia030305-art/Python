def calculate_power(base, exponent):
    result = 1
    for index in range(exponent):
        result *= base
    return result

print(calculate_power(3, 3))  # Output: 27