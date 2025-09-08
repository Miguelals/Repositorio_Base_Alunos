num1 = input("Digite o primeiro numero: ")
num2 = input("Digite o segundo numero: ")

try:
    nume = int(num1)
    num2 = int(num2)

    print(f"A soma dos numeros e: {num1 + num2}")

except:
    print("Digite um numero correto")