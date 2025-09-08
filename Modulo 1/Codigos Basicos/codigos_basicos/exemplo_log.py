nome_arquivo = "exemplo_logs.txt"
palavra_chave = "ERRO"
lista_linhas = ["2025-07-27 INFO: Tudo funcionando bem.","2025-07-27 10:00:05 DEBUG: Processando requisição ID: 123.","2025-07-27 10:00:10 ERRO: Falha ao conectar ao banco de dados."]
quantidade_erros = 0

for linha in lista_linhas:
    if palavra_chave in linha:
        print(linha)

# frutas = ["maça" , "laranja" , "banana"]
# for fruta in frutas:
#     print(f"Eu gosto de {fruta}")


#exemplo avulso
#previsao_tempo = "Previsão do tempo: chuva" 

#if "chuva" in previsao_tempo:
    #print("Previsão de chuva")

#else:
    #print("Não ira chover")
