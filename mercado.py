from typing import List, Dict
from time import sleep

from Models.produto import Produto
from Models.funcoesProdutos import Funcoes
from Models.telas import tela


produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    tela()

    opcao: int = int(input())

    if opcao == 1:
        Funcoes.cadastrar_produto(opcao)
        menu()
    elif opcao == 2:
        Funcoes.listar_produtos(opcao)
        menu()
    elif opcao == 3:
        Funcoes.comprar_produto(opcao)
        menu()
    elif opcao == 4:
        Funcoes.visualizar_carrinho(opcao)
        menu()
    elif opcao == 5:
        Funcoes.fechar_pedido(opcao)
        menu()
    elif opcao == 6:
        print('Obrigado pela preferência.\nVolte Sempre!')
        sleep(4)
        exit(0)
    else:
        print('Opcao Inválida')
        sleep(4)
        main()


if __name__ == '__main__':
    main()
