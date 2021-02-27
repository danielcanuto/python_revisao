#!/usr/bin/python3
def soma_2(a, b):
    return a + b

def soma_3(a, b, c):
    return a + b + c

def soma_n(*args):
    soma = 0
    for n in args:
        soma += n
    return soma


if __name__ == "__main__":
    print(soma_2( 20, 30))
    print(soma_3(10, 20, 30))

    # packing
    print(soma_n(10, 20, 30, 22))
    print(soma_n(10, 20))
    print(soma_n(10))
    print(soma_n(10, 1, 3, 5, 5, 6))

    # unpacking
    tupla_nums = (1, 2, 3)
    print(soma_n(*tupla_nums))

    lista_nums = (1, 2, 4, 8, 16)
    print(soma_n(*lista_nums))