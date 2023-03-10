# Factorial
n = 7
fact = 1

while n > 0:
    fact = fact * n
    n -= 1

print(fact)


def factorial(m):
    if m < 1:
        return 1
    else:
        number = m * factorial(m - 1)
        return number


print(factorial(7))

# Fibonacci
n = 7


def fibonacci(n):
    if n == 1:
        fib = 0
    elif n > 1:
        prev, fib = 0, 1
        for i in range(n-1):
            fib, prev = fib+prev, fib
    else:
        fib = False
    return fib


print(fibonacci(4))


# bad recurrsion
def fibonacci_rec(n):
    if n <= 1:
        fib = n
    else:
        fib = fibonacci_rec(n-1) + fibonacci_rec(n-2)
    return fib


print(fibonacci_rec(4))
