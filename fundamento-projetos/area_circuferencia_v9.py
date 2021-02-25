#!/usr/bin/python3
from math import pi


def circulo(raio):
    circuferencia = pi * (raio ** 2)
    return circuferencia

if __name__ == "__main__":
    raio = float(input("Digite o valor do Raio: "))
    area = circulo(raio)
    print(f'O raio é {area}')
