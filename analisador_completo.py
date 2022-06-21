#ler nome
#ler idade
#ler sexo
#de 4 pessoas

#retornar a média de idade do grupo
# qual o nome do homem mais velho
# quantas mulheres tem menos de 20 anos
soma_idade = 0
maior_idade_homem = 0
nomevelho = ''
total = 0
for i in range(1,5):
    nome = str(input(f"Insira o {i}° nome: ")).strip()
    idade = int(input(f"Insira a {i} idade: "))
    sexo = str(input("Insira 'm' para masculino ou 'f' para feminino: ")).strip()
    soma_idade += idade
    if i == 1 and sexo in 'Mm': #se dentro de sexo existir 'Mm' as variaveis correspondentes receberao os valores
        maior_idade_homem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maior_idade_homem: #se em algum momento da repetição a idade for maior, essa linha colocará no topo dnv
        maior_idade_homem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        total +=1
media_idade = soma_idade / 4
print(f"A média do grupo é: {media_idade}")
print(f"O homem mais velho se chama {nomevelho} e tem {maior_idade_homem} anos")
print(f"Existem {total} mulheres com menos de 20 anos")