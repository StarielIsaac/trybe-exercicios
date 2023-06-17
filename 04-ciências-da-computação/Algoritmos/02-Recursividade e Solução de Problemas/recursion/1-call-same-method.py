def hello(x):
    if (x == 10):
        return

    print("Olá")
    x += 1
    hello(x)


hello(0)
