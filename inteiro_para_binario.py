#receber numeros inteiros
#transformar em binarios
#devolver em bin

numero_int = int(input("Insira seus numeros: "))
print(f"Seu numero inteiro {numero_int} em numeros binarios fica: {(bin(numero_int)[2:])}")