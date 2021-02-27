#!/usr/bin/python3


def resultado_f1(primeiro, segundo, terceiro):
    print(f'1º - {primeiro}')
    print(f'2º - {segundo}')
    print(f'3º - {terceiro}')

if __name__ == "__main__":
    podium = {"primeiro" : "L. Hamilton",
                "segundo": "M. Verstappen",
                "terceiro" : "S.Vettel"}
    resultado_f1(**podium)
    resultado_f1(*podium)