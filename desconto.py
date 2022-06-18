#ler preço do produto
# inserir desconto no preço do produto
#novo preço do produto com desconto

pp = float(input('Insira o preço do produto: R$ '))
desconto = 0.95
pc = desconto * pp
print (f'Seu produto no valor de R${pp:.2f} com desconto de 5% ficou: R${pc:.2f}')
