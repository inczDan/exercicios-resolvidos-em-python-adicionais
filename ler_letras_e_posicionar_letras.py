#Faça um programa que leia uma frase pelo teclado
# e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez
# e em que posição ela aparece a última vez.
conteudo= str(input("Digite seu contexo: ")).strip()
print(f'O conteudo da sua frase é: {conteudo.lower()}')
print(f"A letra 'A' aparece: {conteudo.count('a')} vezes")
print(f"Nas seguintes posições: {conteudo.find('a')+1}")
print(f"E a ultima posição que ela aparece é: {conteudo.rfind('a')+1}")