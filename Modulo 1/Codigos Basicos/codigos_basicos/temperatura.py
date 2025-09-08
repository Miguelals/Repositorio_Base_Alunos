try:
    temperatura = float(input("Digite a temperatura em Celsius: "))

    if temperatura >= 30:
        print("Esta quente!")
    if temperatura >= 20:
        print("Esta agradavel.")
    if temperatura >= 10:
        print("Esta frio!")
    else:
        print("Esta muito frio!")
except:
    print("Ocorreu um erro")
