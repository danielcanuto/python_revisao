#!/usr/bin/python3

dobros = [ i * 2 for i in range(10)]
print(dobros)

def dobrado():
    dobrar = []
    for i in range(10):
        dobrar.append(i * 2)
    return dobrar

print(dobrado())