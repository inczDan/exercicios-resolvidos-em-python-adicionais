#ler salario
#receber %
#calcular aumento em %
#salario com aumento

salario = float(input("Insira o valor do salario : R$"))
aumento_porcentagem = int(input("insira a porcentagem somente numero: "))
aumento = salario * aumento_porcentagem /100
salario_com_aumento = salario+ aumento
print(f"Seu salario inicial era R${salario}, com o aumento de {aumento_porcentagem}% passou a ser R${salario_com_aumento:.2f}")