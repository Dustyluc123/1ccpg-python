aula02a-variaveis.pyprint("ola mundo")
print(7 + 4)
print("7 + 4")
print("7 " + "4") # CONCATENANDO STRINGS
'''
    Comentario 
    de
    mutliplas 
    linhas
'''

#VARIAVEIS
nome = "Lucas"
idade = 26
peso = 60

print("oii \n",nome, idade, peso)
print(f"ola,{nome}!!")

#input -- simulador de forms no cmd
nome = input("Digite o seu nome")
idade = int(input("digite sua idade: "))
peso = float(input("digite se peso: "))

print(nome, idade, peso)
print(idade + 1)

ano_nascimento = 2007
ano_atual = 2026
idade = ano_atual - ano_nascimento
print(f"Sua idade")