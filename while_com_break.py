soma = 0
n = 0
while True:
    x = int(input("zero sai: "))
    if x == 0:
        break
    else:
        n = n+1
        soma = soma+x
print(f"A soma é {soma} e a média {soma/n:.2f}")