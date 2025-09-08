nomes = ["Joaquim", "Maria", "Ana"]
print("Lista inicial: ", nomes)

nomes.append("Carlos")
print("Apos append: ", nomes)

nomes.insert(1, "Fernanda")
print("Apos insert: ", nomes)

nomes[2] = "Paulo"
print("Apos modificação: ", nomes)

del nomes[3]
print("Apos remove: ", nomes)

nomes.remove("Fernanda")
print("Apos remove: ", nomes)

removido = nomes.pop(2)
print(f"Apos pop (removido ' {removido}'):", nomes)

nomes.clear()
print("Apos clear:", nomes)
            