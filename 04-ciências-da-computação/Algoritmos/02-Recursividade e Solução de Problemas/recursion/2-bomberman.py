import time
# Programe a bomba explodindo no Bomberman


def bomb(number: int):
    # Caso base de parada
    time.sleep(1)
    if number == 0:
        print('💥')
        return
    else:
        print(f'-> {number}')

    # aproximar do caso base
    number -= 1
    # chamar o próprio método
    bomb(number)


if __name__ == "__main__":
    bomb(3)
