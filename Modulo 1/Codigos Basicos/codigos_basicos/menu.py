#def soma(n1,n2):
    #print(n1 + n2)

def soma():
    n1 = float(input("Digite o primeiro numero"))
    n2 = float(input("Digite o segundo numero"))
    print(n1 + n2)

def subtracao(n1,n2):
    print(n1 - n2)



while True:
    opçao = input("1 - opção 1\n2 - opção 2\n0 - sair\n")
    
    if opçao == "0":
        print("sair")
        break
    elif opçao == "1":
        soma()
    elif opçao == "2":
       n1 = float(input("Digite o primeiro numero"))
       n2 = float(input("Digite o segundo numero"))
       subtracao(n1,n2)
    else:
        print("OPÇÃO INVALIDA")