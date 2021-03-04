#!/usr/bin/python3
from datetime import datetime

class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concuir(self):
        self.feito = True

    def __str__(self):
        return (f'{self.descricao} (Concluída)' if self.feto else "")