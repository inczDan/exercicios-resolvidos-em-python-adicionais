# algoritmo para o user digitar varios numeros
# captar em lista sem deixar repetir
# organizar todos em order crescente

lista_user = []
while True:
    lista_user.append(int(input("Insira seu numero: ")))
    continuar = str(input("Deseja continuar inserindo numeros? S/N ")).upper()
    if continuar in 'Ss':
        lista_user.append(int(input("Insira seu numero: ")))
        continuar = str(input("Deseja continuar inserindo numeros? S/N ")).upper()
    elif continuar in 'Nn':
        break
    else:
        print("Comando nao reconhecido, tente novamente!")
        continuar = str(input("Deseja continuar inserindo numeros? S/N ")).upper()
lista_user.sort()
print(f"Sua lista numérica ficou assim: ",end='')
for n in lista_user:
    print(n,end=', ')

