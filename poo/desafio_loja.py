#!/usr/bin/python3
from datetime import datetime
from loja import Cliente, Vendedor, Compra


def main():
    cliente = Cliente('Stella Sofia', 4)
    vendedor = Vendedor("Daniel Canuto", 37, 150000)
    compra1 = Compra(cliente, datetime.now(), 512)
    compra2 = Compra(cliente, datetime(2020, 12, 24), 1024)

    cliente.registrar_compra(compra1)
    cliente.registrar_compra(compra2)

    print(f'Cliente: {cliente}', '(adulto)' if cliente.is_adulto() else "")
    print(f'Vendendor: {vendedor}')

    valor_total = cliente.total_compras()
    qnt_compras = len(cliente.compras)

    print(f'Total: {valor_total} com {qnt_compras} compras')
    print(f'Última compra: {cliente.get_data_ultima_compra()}')

if __name__ == "__main__":
    main()
