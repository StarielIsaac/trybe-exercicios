# https://pythontutor.com/live.html#mode=edit
# Problema - É possível criar uma progressão aritmética
#            a partir de uma sequência?

from sorters.bubble_sort import bubble_sort as ordenador

# teste da aula (Cacem bugs)
# def average_mod(nums):
#     return sum(nums) % len(nums) == 0

def can_make_arithmetic_progression(nums):
    if len(nums) < 3:
        return False
    
    sorted_nums = ordenador(nums)
    sorted_nums = nums
    print('Ordenado:', sorted_nums)
    diferenca = sorted_nums[1] - sorted_nums[0]

    for index in range(1, len(sorted_nums)):
        if sorted_nums[index] - sorted_nums[index - 1] != diferenca:
            return False
    return True

if __name__ == "__main__":
    test1 = [1, 3, 5]  # saída: True
    test2 = [3, 6, 1]  # saída: [1, 3, 6] False
    
    test3 = [7, 43, 19, 25, 1, 31, 37, 13]  # saída: True
    # [1	 7	13	19	25	31	37	43] 
    
    test4 = [7, 43, 19, 25, 1, 32, 37, 13]  # saída:
    #  1 ,7	, 13	19	25	32	37	43 # False

    test5 = [1, 2]  # saída: False

    print(f"Entrada {test1} Saída: {can_make_arithmetic_progression(test1)}.")
    print(f"Entrada {test2} Saída: {can_make_arithmetic_progression(test2)}.")
    print(f"Entrada {test3} Saída: {can_make_arithmetic_progression(test3)}.")
    print(f"Entrada {test4} Saída: {can_make_arithmetic_progression(test4)}.")
    print(f"Entrada {test5} Saída: {can_make_arithmetic_progression(test5)}.")

    # print(f"Entrada {test1} Saída: {average_mod(test1)}.")
    # print(f"Entrada {test2} Saída: {average_mod(test2)}.")
    # print(f"Entrada {test3} Saída: {average_mod(test3)}.")
    # print(f"Entrada {test4} Saída: {average_mod(test4)}.")
    # print(f"Entrada {test5} Saída: {average_mod(test5)}.")