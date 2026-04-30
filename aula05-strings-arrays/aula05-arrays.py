lista_frutas = ["maçã", "banana", "laranja"]

print(lista_frutas[0])  # Acessa o primeiro elemento da lista
print(lista_frutas[1])  # Acessa o segundo elemento da lista
print(lista_frutas[2])  # Acessa o terceiro elemento da lista


lista_frutas.append("uva")  # Adiciona um novo elemento à lista
print(lista_frutas)  # Imprime a lista atualizada

qtd_frutas = len(lista_frutas)  # Obtém a quantidade de elementos na lista
print(f"Quantidade de frutas: {qtd_frutas}")  # Imprime a quantidade de frutas na lista

#for indexado
for i in range(qtd_frutas):
    print(f"Fruta: {lista_frutas[i]}")

#for each
for fruta in lista_frutas:
    print(f"Fruta: {fruta}")

#