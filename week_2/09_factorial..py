# Factorial(N) = N * Factorial(N-1_
# ...
# Factorial(1) = 1

#             factorial(1)
# 5 * 4 * 3 * 2 * 1
def factorial(n):  # 1
    if n == 1:     # True
        return 1
    return n * factorial(n - 1)


print(factorial(5))