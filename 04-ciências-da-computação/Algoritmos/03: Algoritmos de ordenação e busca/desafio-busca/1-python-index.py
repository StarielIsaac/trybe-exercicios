x = ["a"] + ["b"] + [1, 2, 3]
print(x)
# Como saber onde esta o 'b' ?
print(x.index("b"))
# E se não existir, exemplo 'z'?
try:
    print(x.index("z"))
except ValueError:
    print("Não achei")
