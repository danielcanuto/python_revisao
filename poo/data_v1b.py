#!/usr/bin/python3

class Data:
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data()
print(Data)

d1.dia = 5
d1.mes = 12
d1.ano = 2019
print(f'{d1.dia}/{d1.mes}/{d1.ano}')
print(d1)

d2 = Data()
d2.dia = 7
d2.mes = 11
d2.ano = 2020
print(d2)
