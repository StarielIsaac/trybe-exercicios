# https://pythontutor.com/live.html#mode=edit

# Dado um array ordenado e um número alvo,
# retorne o índice caso o alvo seja encontrado,
# se não retorne o índice onde o alvo deve ser inserido.
# Você pode assumir que não teremos valores duplicados.

# USANDO BUSCA BINÁRIA
def search_insert(numbers, target):
    low_index = 0
    high_index = len(numbers)

    while low_index < high_index:
        middle_index = (low_index + high_index) // 2

        if numbers[middle_index] < target:
            low_index = middle_index + 1
        else:
            high_index = middle_index

    return low_index


# teste3 = [1, 3, 5, 6]
# alvo3 = 7
# low_index = 6
# high_index = 6
# middle = 5

#   teste1 = 
#    alvo1 = 7

if __name__ == "__main__":
    teste1 = [1, 3, 5, 6, 7]
    alvo1 = 5
    # saída: 2
    print(f"Posição a ser inserido {search_insert(teste1, alvo1)}")

    teste2 = [1, 3, 5, 6]
    alvo2 = 2
    # saída: 1
    print(f"Posição a ser inserido {search_insert(teste2, alvo2)}")

    teste3 = [1, 3, 5, 6]
    alvo3 = 7
    # saída: 4
    print(f"Posição a ser inserido {search_insert(teste3, alvo3)}")

    teste4 = [1, 3, 5, 6]
    alvo4 = 0
    # saída: 0
    print(f"Posição a ser inserido {search_insert(teste4, alvo4)}")
