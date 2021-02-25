PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
textos = [
    "João gosta de futebol e política",
    "A praia foi divertida",
]

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print(f"Texto Possui pelo menos uma palavra proibida: {palavra}")
            found = True
            break

if __name__ == "__main__":
    print("vai")