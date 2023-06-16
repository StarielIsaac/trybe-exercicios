""""
###PROBLEMA:
Dada uma lista de números inteiros, de tamanho n,
percorrer cada elemento da lista e substituí-lo pelo maior valor
que estiver à sua direita na lista. Caso não exista um valor maior à direita
do elemento, o elemento original deve ser mantido.
"""

DESCRIPTION = "Dois loops simples"
TIME_COMPLEXITY = "O(n²)"
SPACE_COMPLEXITY = "O(1)"


def number_substitution(numbers: list[int]):
    for i in range(len(numbers)):
        original_element = numbers[i]
        right_max = original_element

        for j in range(len(numbers)):
            new_element = numbers[j]
            if j > i and new_element > right_max:
                right_max = new_element
            numbers[i] = right_max


if __name__ == "__main__":
    numbers_list = [2, 1, 2, 3, 0, 5, 1, 2, 3]  # 5
    #   resposta = [5, 5, 5, 5, 5, 5, 3, 3, 3]
    # saída =      []

    print("Antes:", numbers_list)
    number_substitution(numbers_list)
    print("Depois:", numbers_list)
