#ler palavras palindromas
frase = str(input("Insira sua frase: ")).strip().upper() # aqui impedimos espaços iniciais e finais, alem de deixar tudo maiusculo
palavras = frase.split() # separamos a frase em uma lista para depois unificarmos com join sem espaços
juntando = ''.join(palavras) # juntamos tudo com join, para apagar os espaços que existiam
inverso = ''
for letra in range(len(juntando) - 1, -1, -1): #esse for esta contando de tras para frente, letra por letra
    inverso += juntando[letra] # esse é o acumulador, letra por letra, literalmente
if inverso == juntando:
    print("Esta palavra é palindrome!")
else:
    print("Isso nao é palindromo oh!")
