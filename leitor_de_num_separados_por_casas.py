#ler numeros de 0 a 9999
#mostrar o numero
#mostrar unidade
#mostrar dezena
#mostrar centena
#mostrar milhar
#
# numero = (input("Insira seu numero de até 4 digitos: "))
# unidade = numero[3]
# dezena = numero[2]
# centena = numero[1]
# milhar = numero[0]
# print(f"unidade: {unidade}")
# print(f"Dezena: {dezena}")
# print(f"Centena: {centena}")
# print(f"Milhar {milhar}")

        #modelo matematico

num = int(input("numero aqui"))
uni = num // 1 % 10
dez = num // 10 % 10
cent = num // 100 % 10
mil = num // 1000 % 10
print(uni)
print(dez)
print(cent)
print(mil)