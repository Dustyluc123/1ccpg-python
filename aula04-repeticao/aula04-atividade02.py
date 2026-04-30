# Escreva um programa que dadas duas notas de 0 a 10
# calcula a média aritmética entre elas.
def validar_nota(nota):
    nota_temp = nota
    while nota_temp < 0 or nota_temp > 10:
        print("A nota deve estar entre 0 e 10")
        nota_temp = float(input("Digite novamente a nota: "))
    return nota_temp

# solicitar e validar a primeira nota
notaA = float(input("Digite a primeira nota: "))
notaA = validar_nota(notaA)

# solicitar e validar a segunda nota
notaB = float(input("Digite a segunda nota: "))
while notaB < 0 or notaB > 10:
    print("A nota deve estar entre 0 e 10")
    notaB = float(input("Digite novamente a segunda nota: "))

# calcular a media
media = (notaA + notaB) / 2
print("A média é", media)