#receba 3 numeros
#retorne o menor
#retorne o maior

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))

if (numero1 > numero2) and (numero1 > numero3):
    print(f"O numero {numero1} é o maior")
elif (numero2 > numero1) and (numero2 > numero3):
    print(f"O numero {numero2} é maior")
else:
    print(f"O numero {numero3} é maior")
if numero1 < numero2 and numero1 < numero3:
    print(f"O menor numero é: {numero1}")
elif numero2 < numero3 and numero2 < numero1:
    print(f"O menor numero é: {numero2}")
else:
    print(f"O menor numero é: {numero3}")