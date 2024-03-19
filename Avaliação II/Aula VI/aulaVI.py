class No:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None

class DuplamenteEncadeada:
    def __init__(self):
        self.primeiro = None
        self.proximo = None

    def vazia(self):
        return self.primeiro is None
    
    def inserir_no_inicio(self, valor):
        new_node = No(valor)
        if self.vazia():
            self.primeiro = new_node
            self.ultimo = new_node
        else:
            new_node.proximo = self.primeiro
            self.primeiro.anterior = new_node
            self.primeiro = new_node
        
    def inserir_no_final(self, valor):
        new_node = No(valor)
        if self.vazia():
            self.primeiro = new_node
            self.ultimo = new_node
        else:
            new_node.anterior = self.ultimo
            self.ultimo.proximo = new_node
            self.ultimo = new_node

    def remover_do_inicio(self):
        if self.vazia():
            return None
        valor_removido = self.primeiro.valor
        if self.primeiro == self.ultimo:
            self.primeiro = None
            self.ultimo = None
        else:
            self.primeiro = self.primeiro.proximo
            self.primeiro.anterior = None
        return valor_removido
    
    def remover_do_final(self):
        if self.vazia():
            return None
        valor_removido = self.ultimo.valor
        if self.ultimo == self.primeiro:
            self.primeiro = None
            self.ultimo = None
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.proximo = None
        return valor_removido
    
    def imprimir(self):
        no_atual = self.primeiro
        while no_atual is not None:
            print(no_atual.valor, end=" ")
            no_atual = no_atual.proximo
        print()

lista = DuplamenteEncadeada()

lista.inserir_no_inicio(90)
lista.inserir_no_inicio(50)
lista.inserir_no_final(33)
lista.inserir_no_final(80)
lista.inserir_no_final(60)

lista.imprimir()

lista.remover_do_inicio()
lista.remover_do_final()

lista.imprimir()
