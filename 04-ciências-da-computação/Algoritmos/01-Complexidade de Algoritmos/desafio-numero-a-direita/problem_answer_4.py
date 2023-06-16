""""
###PROBLEMA:
Dada uma lista de números inteiros, de tamanho n,
percorrer cada elemento da lista e substituí-lo pelo maior valor
que estiver à sua direita na lista. Caso não exista um valor maior à direita
do elemento, o elemento original deve ser mantido.
"""

DESCRIPTION = "1 for"
TIME_COMPLEXITY = "O(n)"
SPACE_COMPLEXITY = "O(1)"


def number_substitution(numbers: list[int]):
    last_position = len(numbers) - 1
    right_max = numbers[last_position]

    for i in range(last_position, -1, -1):
        if right_max >= numbers[i]:
            numbers[i] = right_max
        else:
            right_max = numbers[i]


if __name__ == "__main__":
    numbers_list = [2, 1, 2, 3, 0, 5, 1, 2, 3]  # 5
    #   resposta = [5, 5, 5, 5, 5, 5, 3, 3, 3]
    # saída =      []

    print("Antes:", numbers_list)
    number_substitution(numbers_list)
    print("Depois:", numbers_list)
