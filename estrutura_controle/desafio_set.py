#!/usr/bin/python3 
PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}
textos = [
    "Joãbrao gosta de futebol e política",
    "A praia foi divertida",
]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print("Texto possui palavras proibidas: ", intersecao)
    else:
        print("Texto autorizado: ", texto)
