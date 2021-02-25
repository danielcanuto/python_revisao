produto = {"nome": "Caneta chic", "preço": 14.99, "importado": True, "estoque": 793}

for chave in produto:
    print(chave)
print("primeiro")
for valor in produto.values():
    print(valor)
print("segundo")
for chave, valor in produto.items():
    print(f"{chave} = {valor}")
print("terceiro")