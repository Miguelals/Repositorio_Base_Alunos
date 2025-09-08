print("Valor do usuario")
valor = int(input())

if valor % 2 == 0:
    situacao ="Numero par"
else:
    situacao = "Numero impar"

with open("resultado.txt", "a", encoding="utf-8") as resultado_arquivo:
    resultado_arquivo.write(f"{valor} é {situacao}\n")
