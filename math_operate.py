def power(base, exp):
    return base ** exp


def average(numbers_list):
    return sum(numbers_list) / len(numbers_list)


import math_operate

# Calculate power
result_power = math_operate.power(5, 2)

numbers = [10, 20, 30, 40]
result_average = math_operate.average(numbers)

# Print results
print("5^2 =", result_power)
print("Average =", result_average)