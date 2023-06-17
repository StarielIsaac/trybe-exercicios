def fibonacci(n):
    if n < 2:
        return n
    else:
        print("fibonacci(n-1) + fibonacci(n-2)")
        print(f"{n-1} + {n-2}")

        return fibonacci(n-1) + fibonacci(n-2)
