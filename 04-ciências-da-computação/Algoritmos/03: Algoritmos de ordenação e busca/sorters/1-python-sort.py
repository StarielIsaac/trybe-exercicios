# Como Ordernar um list_1 ?
list_1 = [5, 3, 2, 1]
print('desordenado', list_1)
# list_1.sort()
print('ordenado', sorted(list_1))
print('original', list_1)

# O sorted, aceita para string?
list_2 = "Hoje considero um bom dia para estudar Python"
print(sorted(list_2))

# Da para ordernar por palavra?
list_3 = "Hoje considero um bom dia para estudar Python".split()
print('original', list_3)
print(sorted(list_3, key=str.lower))
