#!/usr/bin/python3

def fibonacci(limite):
    penultimo = 0
    ultimo = 1 
    print(f'{penultimo}, {ultimo}', end=",")
    while ultimo < limite -1:
        proximo = penultimo + ultimo
        print(proximo, end=", ")
        penultimo = ultimo
        ultimo = proximo
    print("")

if __name__ == "__main__":
    fibonacci(20000)
    