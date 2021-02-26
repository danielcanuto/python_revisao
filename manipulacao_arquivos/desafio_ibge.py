#!/usr/bin/python3
import csv


with open("desafio_ibge.csv") as dados:
    cont = 0
    for dado in csv.reader(dados):
        if cont == 0:
            cont = 1
            pass

        else:
            print(f"{dado[8]} - {dado[4]}")
            
