#!/usr/bin/python3
from datetime import datetime


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return (f'{self.descricao} status = Concluída)' if self.feito else "status = Aberto")


def main():
    casa = []
    casa.append(Tarefa("Passar roupa"))
    casa.append(Tarefa("Comprar produtos de limpeza"))
    casa.append(Tarefa("Lavar prato"))
    casa.append(Tarefa("Lavar roupa"))

    [tarefa.concluir() for tarefa in casa if tarefa.descricao == "Lavar prato"]
    print("Check List\n")
    for tarefa in casa:
        print(f'{tarefa}')


if __name__ == "__main__":
    main()
