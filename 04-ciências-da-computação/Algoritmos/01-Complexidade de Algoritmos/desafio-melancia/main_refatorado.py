import climage
import time

frutas = ["melancia", "banana", "pera"]

distanca_ate_feira = 4

# o(n) + o(n)
# o(2n)
# o(n)


def ir_a_feira(coisas_a_fazer):
    x = 0
    while x < distanca_ate_feira:
        time.sleep(1)
        print(f"Percorrendo Km {x}")
        x += 1

    for algo_ao_fazer in coisas_a_fazer:
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


def mostrar_a_melancia_para_chefia():
    print(climage.convert("melancia.png"))


if __name__ == "__main__":
    acoes = [
        check_api_feira_se_tem,
        check_preco,
        check_promocao,
        outras_frutas,
        comprar_melancia,
        mostrar_a_melancia_para_chefia,
    ]

    # for fruta in frutas:
    print(f"Ações para {frutas}?", ir_a_feira(acoes))
