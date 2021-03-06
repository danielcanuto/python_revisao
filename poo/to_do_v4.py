#!/usr/bin/python3
from datetime import datetime, timedelta


class Projeto:
    # metodo construtor
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    # metodo de interaçãõ

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas
                if not tarefa.feito]

    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pentente(s))'


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
           status.append("(Concluído)")
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append("(Vencida")
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f"(Vence em {dias} dias)")
        return f'{self.descricao} ' + " ".join(status)


def status_projeto(projeto):
    # for tarefa in projeto.tarefas:
    for tarefa in projeto:
        print(f'-{tarefa}')
    
    print(projeto)
    print("\n")

def main():


    casa = Projeto('Tarefas de Casa')
    casa.add("Passar roupa", datetime.now())
    casa.add("Lavar prato")
    status_projeto(casa)


    casa.procurar("Lavar prato").concluir()
    status_projeto(casa)


    mercado = Projeto("Compras Mercado")
    mercado.add("Frutas seca")
    mercado.add("Carne", datetime.now() + timedelta(days=3, minutes=12))
    mercado.add("Tomate")
    print(mercado)
    status_projeto(mercado)

    compra_carne = mercado.procurar("Carne")
    compra_carne.concluir()
    status_projeto(mercado)


if __name__ == "__main__":
    main()
