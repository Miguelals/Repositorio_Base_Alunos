
listar_nomes = []



while True:
    opcao = input("Programa de Agenda\n1 - Cadastrar pessoas\n2 - Listar pessoa\n3 - Excluir pessoa\n0 - Sair\n")

    if opcao == "0":
        print("Saindo do programa...")
        break
    elif opcao == "1":
        nome = input("Digite o nome que deseja adicionar: ")
        listar_nomes.append(nome)
        print(listar_nomes)

    elif opcao == "2":
        print(listar_nomes) 
    
    elif opcao == "3":
        print("Excluir") 
        print(listar_nomes)
    else:
        print("Opção inválida.")
