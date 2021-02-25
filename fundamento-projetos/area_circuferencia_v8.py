#!/usr/bin/python3
from math import pi


def circulo(raio):
    circuferencia = pi * (raio ** 2)
    print(f"Area do circulo {circuferencia}")

if __name__ == "__main__":
    raio = float(input("Digite o valor do Raio: "))
    circulo(raio)
