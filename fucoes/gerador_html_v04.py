#!/usr/bin/python3


def tag_bloco(conteudo, *args, classe="success", inline=False):
    tag = "span" if inline else "div"
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}">\n{html}\n</{tag}>'


def tag_lista(*itens):
    lista_html = "".join(f'<li>{item}</li>\n' for item in itens)
    return f'<ul>\n{lista_html}</ul>'


if __name__ == "__main__":
    print(tag_bloco('bloco'))
    print(tag_bloco("inline e classe", "info", True))
    print(tag_bloco("inline", inline=True))
    print(tag_bloco("inline", inline=True))
    print(tag_bloco(inline=True, conteudo="inline"))
    print(tag_bloco("falhou", classe="error"))
    print(tag_bloco("falhou", "error"))  # Mesma coisa do de cima

    print(tag_lista("Daniel", "Simone", "Stella"))
    print(tag_bloco(tag_lista("Daniel", "Simone", "Stella")))

    print(tag_bloco(tag_lista, "sábado", "domingo", classe='info'))
    print(tag_bloco(tag_lista, "sábado", "domingo", classe='info', inline=True))
    # print(tag_bloco("Eu sei que é isso mesmo"))

    # print(tag_bloco("Eu sei que é isso mesmo", "truta"))
