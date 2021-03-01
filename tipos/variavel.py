# -*- coding: utf-8 -*-
#!python3
a = 3
b = 4.4
print(a + b)

texto = "Sua idade é ..."
idade = 23

# print(texto + str(idade))
print(f'{texto} {idade}')

vozes = "opa"
print( 3 * "bom dia ")
print( 3 * vozes)

# convençao de CONSTANTES                       

PI = 3.14
raio = float(input('Informe o raio da circuferencia: '))
area = PI * pow(raio, 2)
print(raio)
print(PI * raio)
print(area)
print(f'A área da circuferencia é de {area} m².')