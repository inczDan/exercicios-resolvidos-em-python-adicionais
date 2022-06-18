    #calcular imc e devolver indice
#receber peso
#receber altura
# calcular de acordo com imc
#encaixar resultado na tabela de acordo com indice
#devolver indice de resultado

peso_user = float(input("Insira seu peso em kg: "))
altura_user = float(input("Insira sua altura em cm: "))
imc = (peso_user / (altura_user * altura_user))*10000

if imc <= 18.5:
    print(f"Seu IMC é {imc:.2f}. Você está abaixo do peso ideal.")
elif imc <= 25:
    print(f"Seu IMC é {imc:.2f}. Você está com o peso ideal.")
elif imc <= 30:
    print(f"Seu IMC é {imc:.2f}. Você está sobrepeso.")
elif imc <= 40:
    print(f"Seu IMC é {imc:.2f}. Você está obeso.")
else:
    print(f"Seu IMC é {imc:.2f}. Você está em grau de obesidade morbida.")