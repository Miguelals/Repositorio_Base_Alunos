print("Digite o nome do aluno")
nome = input()
print("Insira sua primeira nota")
nota1 = input()
print("insira sua segunda nota")
nota2 = input()
print("Insira sua terceira nota")
nota3 = input()

nota1=float(nota1)
nota2=float(nota2)
nota3=float(nota3)

resultado = nota1 + nota2 + nota3 
media = resultado / 3

if media >= 7:
    situacao = "aprovado"

elif media > 4:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

with open("media.txt", "a", encoding="utf-8") as media_arquivo:
    media_arquivo.write(f"{nome} com média {media:.1f} está: {situacao}\n")

