#fzr o pc pensar em um numero int de 0 a 5
# entrada para o usuario tentar acertar o numero
#imprimir na tela se o numero informado esta correto
import random

num_usuario = int(input("Está com sorte hoje? Tente um numero de 0 a 5:  "))
num_possiveis = [0, 1, 2, 3, 4, 5]
numeros =  random.choice(num_possiveis)
if num_usuario == numeros:
    print(f"O numero escolhido foi: {numeros}! Meus parabens!")
elif num_usuario != numeros:
    print(f"Você errou o numero era {numeros}, tente novamente!")
