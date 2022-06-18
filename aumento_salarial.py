#receber o salario da pessoa em float
#calcular o aumento de acordo com as porcentagens
# > 1.250,00 aumento de 10%
# <= 1.250,00 aumento de 15%

salario = float(input("Insira seu salario: "))

if salario <= 1250.00:
    novo_salario = salario * 1.15
elif salario:
    novo_salario =  salario * 1.10
print(f"Seu novo salario é: {novo_salario:.2f}, o antigo era: {salario:.2f} o aumento em R$ foi de: {novo_salario - salario:.2f}")