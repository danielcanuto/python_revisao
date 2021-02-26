#!/usr/bin/python3

dobros = [ i * 2 for i in range(10) if i % 2 == 0]
print(dobros)

def dobrado_par():
    dobrar = []
    for i in range(10):
        if i % 2 == 0:
            dobrar.append(i * 2)
    return dobrar

print(dobrado_par())