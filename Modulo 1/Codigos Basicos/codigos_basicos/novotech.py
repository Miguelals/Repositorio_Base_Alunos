
def soma(n1,n2):
    return n1 + n2

def subtrair(n1,n2):
    return n1 - n2

def multiplicar(n1,n2):
    return n1 * n2

def dividir(n1,n2):
    return n1 / n2

try:
    numero1= int(input("Digite o primeiro numero: "))
    numero2= int(input("Digite o segundo numero: "))

    opcao = input("Digte a opção que deseja: \n1 - Soma\n2 - Subtração\n3 - multiplicação\n4 - Divisão\n")



    if opcao == "1":
        print(f"A soma dos numeros e: {soma(numero1,numero2)}")
    elif opcao == "2":
        print(f"A Subtração dos numeros e: {subtrair(numero1,numero2)}")
    elif opcao == "3":
        print(f"A multiplicação dos numeros e: {multiplicar(numero1,numero2)}")
    elif opcao == "4":
        print(f"A divisão dos numeros e: {dividir(numero1,numero2)}")
    else:
        print("TA ERRADO PARCEIRO")
except:
    print("Ocorreu um erro")

















