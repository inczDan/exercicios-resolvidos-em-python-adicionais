# mostrar os 5 primeiros
# os ultimos 4
# todos em ordem alfabetica
# a posição do Gremio



times = ('Intercional', 'Vasco da Gama', 'Atlético-MG', 'Palmeiras', 'São Paulo', 'Santos', 'Fluminense', 'Bahia',
              'Grêmio', 'Athletico-PR', 'Botafogo', 'Bragantino-SP', 'Flamengo', 'Corinthians', 'Goiás', 'Fortaleza',
              'Atlético-GO', 'Sport Recife', 'Ceará SC', 'Coritiba')

print("=-"*10)
print("Os Primeiros 5 times")
print(times[:5])
print("=-"*10)
print("=-"*10)
print("Os ultimos 4 times")
print(times[-4:])
print("=-"*10)
print("=-"*10)
print("todos os times, em ordem alfabetica")
print(sorted(times))
print("=-"*10)
print("=-"*10)
print("em que posição o 'Grêmio' esta?")
print(times.index('Grêmio'))


