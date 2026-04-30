cp = 0

while cp < 3:
    print(f"Produto {cp}")
    cp = cp + 1

# while decrescente
i = 4

while i > 0:
    print(i)
    i -= 1

# repetição com entrada de usuario
jogar = "SIM"

while jogar.lower() == "sim":
    print("Repete ou inicia o jogo")
    jogar = input("Deseja jogar novamente?")

# MODIFICADORES DE LAÇO break - continue

i = 0

while i < 10:
    i += 1

    if i == 3 or i == 5:
        continue

    if i == 7:
        break

    print(f"Produto {i}")
