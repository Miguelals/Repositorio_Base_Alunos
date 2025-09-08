print("Insira sua altura")
altura=input()
print("Insira seu peso")
peso=input()
try:
    altura=float(altura)
    peso=float(peso)


    resultado = altura * altura
    imc = peso / resultado
    if imc >= 40:
        print("Obesidade Grau III")
    elif imc >= 39.9:
        print("Obesidade Grau II")
    elif imc >= 34.9:
        print("Obesidade Grau I")
    elif imc >= 29.9:
        print("SobrePeso")
    elif imc >= 24.9:
        print("Peso Normal")
    elif imc >= 18.5:
        print("Abaixo do Peso")
    else:
        print("Fino do Fino")
except:
    print("Ocorreu um erro")

