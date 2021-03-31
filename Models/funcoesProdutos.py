from time import sleep
from typing import List, Dict

from Models.telas import tela_checagem_produto, separa_linha
from Models.produto import Produto
from Utils.helper import converte_float_para_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


class Funcoes:

    def cadastrar_produto(self: int) -> None:
        print('Cadastro de Produto: ')
        print('---------------------')

        nome: str = input('Informe o Nome do Produto: ')
        preco: float = float(input('Informe o Preco do Produto: '))

        produto: Produto = Produto(nome, preco)

        produtos.append(produto)

        print(f'Produto : {produto.nome} foi Cadastrado com Sucesso.')

        sleep(2)

    def listar_produtos(self: int) -> None:
        if len(produtos) > 0:
            print('Listagem de Produtos')
            print('--------------------')
            for Produto in produtos:
                print(Produto)
                separa_linha()
        else:
            print('Lista de Produtos Vazia')
        sleep(2)

    def comprar_produto(self: int) -> None:
        if len(produtos) > 0:
            tela_checagem_produto()
            for produto in produtos:
                print(produto)
                separa_linha()
                sleep(1)
            codigo: int = int(input())

            produto: Produto = pegar_produto_pelo_codigo(codigo)

            if produto:
                if len(carrinho) > 0:
                    tem_no_carrinho: bool = False
                    for item in carrinho:
                        quant: int = item.get(produto)
                        if quant:
                            item[produto] = quant + 1
                            print(f'O produto {produto.nome} agora possui {quant + 1} unidade(s) no carrinho')
                            tem_no_carrinho = True
                            sleep(2)
                    if not tem_no_carrinho:
                        prod = {produto: 1}
                        carrinho.append(prod)
                        print(f'O produto: {produto.nome}, foi acidionado ao carrinho')
                        sleep(2)
                else:
                    item = {produto: 1}
                    carrinho.append(item)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho')
                    sleep(2)
            else:
                print(f'O Produto com codigo: {codigo} , não foi encontrado')
        else:
            print('Ainda não existem produtos cadastrados para venda.')
            sleep(2)

    def visualizar_carrinho(self: int) -> None:
        if len(carrinho) > 0:

            print('Produtos do Carrinho: ')
            for item in carrinho:
                for dados in item.items():
                    print(dados[0])
                    print(f'Quantidade: {dados[1]}')
                    print('-------------------------------')
                    sleep(1)
        else:
            print('Ainda nao existem produtos no carrinho.')
            sleep(2)

    def fechar_pedido(self: int) -> None:
        if len(carrinho) > 0:
            valor_total: float = 0

            print('Produtos do Carrinho: ')
            for item in carrinho:
                for dados in item.items():
                    print(dados[0])
                    print(f'Quantidade: {dados[1]}')
                    valor_total += dados[0].preco * dados[1]
                    print('-------------------------------')
                    sleep(1)
                print(f'Sua Fatura e {converte_float_para_str_moeda(valor_total)}')
                print('Obrigado pela preferência\nVolte Sempre!')
                carrinho.clear()
                sleep(5)
        else:
            print('Carrinho Vazio.')
            sleep(2)

def pegar_produto_pelo_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p
