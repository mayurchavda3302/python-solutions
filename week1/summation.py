def sum_of_digits_iterative(num):
    total = 0

    while num > 0:
        total += num % 10
        num //= 10

    return total


num = 12345
print("Sum of Digits (Iterative):", sum_of_digits_iterative(num))