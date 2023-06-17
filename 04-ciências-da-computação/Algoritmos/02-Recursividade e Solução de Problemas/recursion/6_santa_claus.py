def entregar_presentes_de_natal(casas):
    print("Casas para sem entregues", casas)

    if (len(casas) == 1):
        print("Entregando o presente na casa", casas[0])
    else:
        metade = len(casas) // 2
        primeira_metade = casas[:metade]
        segunda_metade = casas[metade:]

        entregar_presentes_de_natal(primeira_metade)
        entregar_presentes_de_natal(segunda_metade)


casas = [
    "Casa do Ben",
    "Casa do Phelps",
    "Casa do Melqui",
    "Casa da Laura",
    "Casa do Pedro",
    "Casa do Will",
]

entregar_presentes_de_natal(casas)

# Call 1
# Ajudante 1 = ["Casa do Ben", "Casa do Phelps", "Casa do Melqui"]

# Call 1.2
# Ajudante 2 = ["Casa do Ben", "Casa do Phelps"]

# Call 1.2
# Ajudante 3 = ["Casa do Melqui", "Casa da Laura"]

# Call 1.2.1
# Ajudante 4 = ["Casa do Ben"]

# Call 1.2.2
# Ajudante 5 = ["Casa do Phelps"]

# Call 1.2.2
# Ajudante 6 = ["Casa do Melqui"]

# Call 1.2.2
# Ajudante 7 = ["Casa da Laura"]


# Primeiro: Ajudante 3
# Segundo: Ajudante 4
# Terceiro: Ajudante 6
# Quarto: Ajudante 7