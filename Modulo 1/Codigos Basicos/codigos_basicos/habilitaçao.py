nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? "))
possui_carteira = input("Possui carteira de motorista? /n (1-sim ? 2-não) ")

if idade >= 18:
    if possui_carteira == "1":
        print("Pode dirigir")
    else:
        print("Não pode dirigir")
else:
    print("Menor de idade")