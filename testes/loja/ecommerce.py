class Produto:
    def __init__(self, nome = '', preco = 0.0):
        self.nome = nome
        self.preco = preco


class CarrinhoDeCompra:
    def __init__(self):
        self.carrinho = []
        
    def adicionaProduto(self, produto):
        self.carrinho.append(produto)

    def calculaTotalDeCompras(self):
        total = 0
        for produto in self.carrinho:
            total += produto.preco

        return total