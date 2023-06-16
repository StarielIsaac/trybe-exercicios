import time

fruta = "melancia"

distanca_ate_feira = 4


def ir_a_feira(coisas_a_fazer):
    # o(n)
    # o(nˆ2)

    # o(nˆ2)


    for algo_ao_fazer in coisas_a_fazer:
        x = 0
        while x < distanca_ate_feira:
            time.sleep(1)
            print(f"Percorrendo Km {x}")
            x += 1
        algo_ao_fazer()


    for algo_ao_fazer in coisas_a_fazer:
        x = 0
        while x < distanca_ate_feira:
            time.sleep(1)
            print(f"Percorrendo Km {x}")
            x += 1
        algo_ao_fazer()

    return "Tudo realizado"


def check_api_feira_se_tem():
    return "Sim temos o que precisa."


def check_preco():
    return "R$ 10,00"


def check_promocao():
    return "20% desconto para 5 unidades"


def outras_frutas():
    return "Pera, Jabuticaba, Laranja"


def comprar_melancia():
    return "Melancia Comprada"


if __name__ == "__main__":
    acoes = [
        check_api_feira_se_tem,
        check_preco,
        check_promocao,
        outras_frutas,
        comprar_melancia,
    ]

    print(f"Ações para {fruta}?", ir_a_feira(acoes))