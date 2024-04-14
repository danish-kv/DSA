# def fibonacci(n):
#     if n <= 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# p = fibonacci(10)
# print('fibonacci', p)


# Write a recursive function to find the sum of digits of a positive integer.

# def sum_of_digits(n):
#     if n < 10:
#         return n
#     else:
#         return n % 10 + sum_of_digits(n // 10)
#
#
# p = sum_of_digits(12345)
# print(p)


# Write a recursive function to calculate the factorial of a non-negative integer.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
