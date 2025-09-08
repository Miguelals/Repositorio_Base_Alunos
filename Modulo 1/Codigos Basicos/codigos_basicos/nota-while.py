i = 1

while i <= 3:
    
    nome = input("Digite seu nome")
    n1 = float(input("Digite sua primeira nota"))
    n2 = float(input("Digite sua segunda nota"))
    n3 = float(input("Digite sua terceira nota"))

    resultado = n1 + n2 + n3
    media = resultado/3
    print(f"O aluno: {nome}, teve media: {media:.1f}")
    i = i + 1
    


