#!/usr/bin/python3

def todos_parms(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


if __name__ == "__main__":
    todos_parms("a", "b", "c")
    todos_parms("a", "b", "c", legal= True, agora="vamos", idade=33)
    todos_parms("Ana", False, [1, 2, 3], tamanho="M", fragil=False)
    # todos_parms(primeiro="Daniel","a", "b", "c")
    todos_parms("a", "b", "c", primeiro="Daniel")
    