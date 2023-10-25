from functools import lru_cache


def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)


def add_positive_numbers(a: int, b: int) -> int:
    if a < 0 or b < 0:
        raise ValueError("Both numbers must be positive")
    return a + b


@lru_cache
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Negative arguments are not supported!")

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
