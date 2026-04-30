#criando todas as duplas

duplas = ["Lucas", "Maria", "João", "Ana"]
qtd_duplas = len(duplas)
#imprimindo as duplas
for i in range(qtd_duplas):
    for y in range(i + 1, qtd_duplas):
        print(f"{duplas[i]} e {duplas[y]}")

