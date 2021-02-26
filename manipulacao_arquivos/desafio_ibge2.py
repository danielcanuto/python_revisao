#!/usr/bin/python3
import csv
from urllib import request

def read(url):
    with request.urlopen(url) as entrada:
        cont = 0
        print("baixando o CSV...")
        dados = entrada.read().decode("latin1")
        print("Download Concluído")


        for dado in csv.reader(dados.splitlines()):
            if cont == 0:
                cont = 1
                pass

            else:
                print(f"{dado[8]} - {dado[3]}")
                
if __name__ == "__main__":

    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
