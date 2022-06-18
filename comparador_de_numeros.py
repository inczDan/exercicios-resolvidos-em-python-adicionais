#ler dois numeros
#os comparar
#mostrar se o primeiro é maior
#ou se o segundo é maior
#se ambos forem iguais

primeiro_num = int(input("insira o primeiro numero; "))
segundo_num = int(input("Insira o segundo numero: "))

if primeiro_num == segundo_num:
    print("Uau os numeros sao iguais!")
elif primeiro_num > segundo_num:
    print(f"O primeiro numero ({primeiro_num}) é maior que o segundo numero ({segundo_num})")
else:
    print(f"O segundo numero ({segundo_num}) é maior que o primeiro numero ({primeiro_num})")