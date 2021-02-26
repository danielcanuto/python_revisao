#!/usr/bin/python3

dicionaio = {i: i * 2 for i in range(10) if i % 2 == 0}
print(dicionaio)


for numero, dobro in dicionaio.items():
    print(f'{numero} x 2 = {dobro}')