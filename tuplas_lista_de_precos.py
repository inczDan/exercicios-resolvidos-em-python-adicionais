#criar uma lista de produtos e precos com uma unica tupla de maneira tabular

produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)
print("=-"*10,end=' ')
print("Kalotes papelaria",end=' ')
print("-="*10,end='' "\n")
print(f"""  Lista de produtos:""")
for pos in range(0, len(produtos)): #este for pega o numero da lista como limite
    if pos % 2 ==0: # este if faz com que peguemos só itens de posição par, que no caso serao somente as strings
        print(f"{produtos[pos]:.<30}",end='')
    
