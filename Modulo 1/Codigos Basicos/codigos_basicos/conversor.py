cotacao_dolar = 5.69

def dolar_real(dolares):
    return dolares * cotacao_dolar
def real_dolar(reais):
    return reais / cotacao_dolar
try:
    print("Programa de conversão monetaria\n [1] - converter dolar para real\n [2] - Converter real para dolar ")
    opcao = input("Defina sua opção")
    if opcao =="1":
        dolares = float(input("Digite a quantidade de dolares: "))
        print(f"Voce tem R$ {dolar_real(dolares):.2f}")
    elif opcao =="2":
        reais = float(input("Digite a quantidade de reais: "))
        print(f"Voce tem R$ {real_dolar(reais):.2f}")
    else:
        print("Conversão invalida")
except:
    print("Ocorreu um erro")


