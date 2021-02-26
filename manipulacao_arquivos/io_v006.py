#!/usr/bin/python3

with open("pessoas.csv") as arquivo:
    with open("pessoa.txt", "w") as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(",")
            print('Nome: {}, Idade:{}'.format(*pessoa), file=saida)

if arquivo.closed:
    print("Arquivo já foi fechado!")

if saida.closed:
    print("Arquivo de saída já foi fechado!")