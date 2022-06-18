#fazer um programa que diga se a palavra lida de tras para frente é igual a leitura normal

palavra_user = str(input("Insira a palavra: "))

palindrome = palavra_user == palavra_user[::-1]

print(f"A palavra {palavra_user}, é palindrome? {palindrome} ")
