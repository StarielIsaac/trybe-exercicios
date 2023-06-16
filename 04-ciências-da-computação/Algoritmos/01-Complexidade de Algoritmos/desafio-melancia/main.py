import time

fruta = "melancia"

distanca_ate_feira = 4


def ir_a_feira(algo_ao_fazer):
    x = 0
    while (x < distanca_ate_feira):
        time.sleep(1)
        print(f'Percorrendo Km {x}')
        x += 1
    return algo_ao_fazer()


def check_api_feira_se_tem():
    return ("Sim temos o que precisa.")


def check_preco():
    return "R$ 10,00"


def check_promocao():
    return "20% desconto para 5 unidades"


def outras_frutas():
    return "Pera, Jabuticaba, Laranja"


def comprar_melancia():
    return "Melancia Comprada"


if __name__ == "__main__":
    print(f'Tem {fruta}?', ir_a_feira(check_api_feira_se_tem))
    print(f'Tem {fruta}?', ir_a_feira(check_preco))
    print(f"Promoção {fruta}?", ir_a_feira(check_promocao))
    print(f"Outras Frutas {fruta}? ", ir_a_feira(outras_frutas))
    print(f"Pode comprar {fruta}!", ir_a_feira(comprar_melancia))
