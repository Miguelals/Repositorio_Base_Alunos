def calcula_imc(peso, altura):
    return peso / (altura * altura)

def tabela_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso", "info"
    elif imc < 25:
        return "Peso normal", "success"
    elif imc < 30:
        return "Sobrepeso", "warning"
    elif imc < 35:
        return "Obesidade I", "warning"
    elif imc < 40:
        return "Obesidade II", "error"
    else:
        return "Obesidade III", "error"