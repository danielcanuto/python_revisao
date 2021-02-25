#!/usr/bin/python3

def conceito_nota(nota):
    nota = float(nota)
    if nota > 10 or nota < 0:
        print("Nota inválida")
    
    elif nota >= 9.1:
        print("A")
    elif nota >= 8.1:
        print ("-A")
    elif nota >= 7.1:
        print ("B")
    elif nota >= 6.1:
        print ("-B")
    elif nota >= 5.1:
        print ("C")
    elif nota >= 4.1:
        print ("-C")
    elif nota >= 3.1:
        print ("D")
    elif nota >= 2.1:
        print ("-D")
    elif nota >= 1.1:
        print ("E")
    elif nota >= 0:
        print("-E")

if __name__== "__main__":
    valor_informado = input("Nota do Aluno: ")
    conceito = conceito_nota(valor_informado)
    