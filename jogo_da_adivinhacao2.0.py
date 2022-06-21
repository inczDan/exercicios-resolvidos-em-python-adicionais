#receber entrada int de 0, 10
# o computador ira escolher um numero
# o usuario ficará em loop até acertar
# o num nao muda
#retornar quando acertar:
#o numero e quantas tentativas foram feitas
from random import randint
tentativas = 1
numero_pc = randint(0, 10)
print("Olá, eu sou seu pc, vim te desafiar haha!!")
number_user = int(input("Adivinhe qual numero escolhi! Insira um numero de 0 a 10: "))
while number_user != numero_pc:
    number_user = int(input("Insira o numero correto: "))
    if number_user < numero_pc:
        print("É um pouquinho maisss, vamos lá!")
    if number_user > numero_pc:
        print("Abaixa a mão, vamo com calmaaaa")
    tentativas += 1
print(f"Parabéns, voce acertou! o numero é {numero_pc} e utilizou {tentativas} tentativas")