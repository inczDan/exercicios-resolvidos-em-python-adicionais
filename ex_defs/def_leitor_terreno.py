#criar uma def que execute a area de um terreno

def terreno_area(largura, comprimento):
    area = largura * comprimento
    print(f"a largura é {largura}m, o comprimento é {comprimento}m. O total da area é: {area}²m ")


lar = float(input("Insira a largura: "))
compr = float(input("insira o comprimento: "))
terreno_area(lar, compr)