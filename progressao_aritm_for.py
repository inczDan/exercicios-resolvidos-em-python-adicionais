#algoritimo que recebe o primeiro termo de uma PA
#Recebe a razao
#mostre 10 primeiros termos da progressao

termo = int(input("Insira o termo de sua PA: "))
razao = int(input("Insira a razão de sua PA: "))
decimo = termo + (10 - 1) * razao
for i in range(termo, decimo+razao, razao):
    print(i,end="' ")