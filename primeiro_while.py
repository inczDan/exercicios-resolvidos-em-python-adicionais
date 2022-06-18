#receber um numero do usuario
#criar um while para correr até ele
numero_usuario = int(input("Insira seu numero de 0 a 100: "))
x = 0
if numero_usuario <= 100:
    while x <= numero_usuario:
        print(x)
        x = x + 1
else:
    while numero_usuario > 100:
        print("erro, eu falei que era de 0 a 100 meo!!!")
        numero_usuario = int(input("Insira seu numero de 0 a 100: "))
        if numero_usuario <= 100:
            while x <= numero_usuario:
                print(x)
                x = x + 1

