palavras = str(input("palavras: "))
k = 0
troca = ''
while k < len(palavras):
    if palavras[k] in 'aeiou':
        troca = troca + '*'
    else:
        troca = troca + palavras[k]
    k = k +1
print(troca)