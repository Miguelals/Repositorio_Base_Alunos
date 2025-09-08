try:
    print("Digite o primeiro numero") # Print exibe a informção 
    numero = int(input()) #variavel= lugar para guardar as informações int= transforma texto em numero input= Pega tudo que o usario digitar
    i=1


    while i <= 10: #Laço de repitição
        print(numero * i) #Mostra uma multiplicação
        i = i + 1 #Mostra uma adição
except:
    print("Ocorreu um erro")
