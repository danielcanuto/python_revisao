PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
textos = [
    "João gosta de futebol e política",
    "A praia foi divertida",
]

for texto in textos:

    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print(f"Texto Possui pelo menos uma palavra proibida: {palavra}")
            break
    else:
        print("Texto autorizado")
if __name__ == "__main__":
    print("vai")