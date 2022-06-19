#ler seis numeros inteiros
#mostrar a soma somente daqueles que forem pares
# se o valor for impar, desconsiderar
soma = 0
for i in range(1, 7):
    numeros = int(input(f"insira seu {i}° numero: "))
    if numeros % 2 == 0:
        soma += numeros
print(f"A soma dos numeros pares foi: {soma}")
