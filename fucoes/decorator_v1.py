#!/usr/bin/python3

def log (funcion):
    def decorator(*arg, **kwarg):
        print(f"Inicio da chamada da função: {funcion.__name__}")
        print(f"args: {arg}")
        print(f"kwargs: {kwarg}")

        resultado = funcion(*arg, **kwarg)
        print(f'Resultado da chamada: {resultado}')


        return resultado
    return decorator



@log
def soma(x, y):
    return x + y


@log
def sub(x,y):
    return x - y



if __name__ == "__main__":

    print(soma(5, 7))
    print(sub(4, y=8))
