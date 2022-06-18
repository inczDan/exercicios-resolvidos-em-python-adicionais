#calcular fatorial
number_user = int(input("Insira o numero: "))
fator = 1
k = 1
while k <= number_user:
    fator = fator * k
    k = k+1
    print(f"fat({number_user}) = {fator}")