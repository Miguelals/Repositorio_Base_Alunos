caminho_arquivo = "./atividade_log/logs.txt"
palavra_chave = "ERRO"

with open(caminho_arquivo, 'r', encoding="utf-8") as logs:
    for linha in logs:
        if palavra_chave in linha:
            print(linha.strip())
        

# if palavra_chave in caminho_arquivo:
#     print(f"A palavra_chave '{palavra_chave}' foi encontrada")
# # import os
# print(os.getcwd())






















#1 abrir o arquivo de log
#2 utilizar o for para percorrer a lista
#3 usar o if
#4 identificar a palvra erro
#5 marcar a palvra erro
