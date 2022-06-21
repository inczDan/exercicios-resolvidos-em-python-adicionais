#utilizando tuplas, pegue o maior e menor numero contido nelas
#faça um sorteio pegando esses dois numeros da tupla
import random
#numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
numeros_aleatorios = (random.randint(0, 30), random.randint(0, 30), random.randint(0, 30), random.randint(0, 30), random.randint(0, 30))
# COLOCAMOS O RANDINT EM UMA TUPLA E ISSO FAZ COM QUE CONSIGAMOS REPETIR ELE QUANTAS VEZES QUISERMOS. O RESULTADO VEM EM UMA TUPLA!
# numeros_tuplados = str(numeros_aleatorios)
menor_valor = min(numeros_aleatorios)
maior_valor = max(numeros_aleatorios)
print(f"Os numeros foram {numeros_aleatorios}, maior valor é: {maior_valor}, e o menor valor é: {menor_valor}")