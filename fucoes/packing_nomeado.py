#!/usr/bin/python3

def resultado_f1(**podiom):
    for posicao, piloto in podiom.items():
        print(f'{posicao} -> {piloto}')

if __name__ == "__main__":
    resultado_f1(primeiro="L. Hamilton",
                segundo="M. Verstappen",
                terceiro="S.Vettel")