# Some os inteiros anteriores de um número

# def sum_to(number: int) -> int:
#     pass

# Josué
def sum_to(n):
    if n == 0:
        return 0
    return n + sum_to(n - 1)


# Tulio
def sum_recursive(n):
    if n == 0:
        return 0
    else:
        return n + sum_recursive(n - 1)


if __name__ == "__main__":
    # 4
    # 4 + 3 + 2 + 1 + 0 = 10
    # 6
    # 6 + 5 + 4 + 3 + 2 + 1 + 0 = 21
    print('Josué')
    print(sum_to(4))

    print('Tulio')
    print(sum_recursive(4))
