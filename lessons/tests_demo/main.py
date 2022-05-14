def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    print(fibonacci(0))
