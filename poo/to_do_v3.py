#!/usr/bin/python3
from datetime import datetime


class Projeto:
    # metodo construtor
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

        
    # metodo de interaçãõ
    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas
                if not tarefa.feito]

    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pentente(s))'


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + " - " + ('status = Concluída)' if self.feito else "status = Pendente")


def status_projeto(projeto):
    # for tarefa in projeto.tarefas:
    for tarefa in projeto:
        print(f'-{tarefa}')
    
    print(projeto)
    print("\n")

def main():


    casa = Projeto('Tarefas de Casa')
    casa.add("Passar roupa")
    casa.add("Lavar prato")
    status_projeto(casa)


    casa.procurar("Lavar prato").concluir()
    status_projeto(casa)


    mercado = Projeto("Compras Mercado")
    mercado.add("Frutas seca")
    mercado.add("Carne")
    mercado.add("Tomate")
    print(mercado)
    status_projeto(mercado)

    compra_carne = mercado.procurar("Carne")
    compra_carne.concluir()
    status_projeto(mercado)


if __name__ == "__main__":
    main()
