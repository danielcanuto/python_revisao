#!/usr/bin/python3
from math import pi
import sys

def circulo(raio):
    circuferencia = pi * (raio ** 2)
    return circuferencia

if __name__ == "__main__":
    raio = sys.argv[1]
    area = circulo(raio)
    print(f'O raio é {area}')
