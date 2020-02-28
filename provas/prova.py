from datetime import datetime

class Pessoa:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade


    def __str__(self):
        print(f'nome: {self.nome}\nidade: {self.idade}')


    #def is_adulto(self):


class Vendedor(Pessoa):
    def __init__(self,nome, idade, salario):
        super().__init__(nome,idade)
        self.salario = salario

    



class Cliente(Pessoa):
    def __init__(self,nome,idade):
        super().__init__(nome,idade)
        self.compras = []
        

    def registrar_compra(self,compra):
        return self.compras.append(compra)
        #super().__str__()
        

    #def get_data_ultima_compra(self):
        #return datetime


    def total_compras(self,somatorio=0):
        for item in self.compras:
            somatorio+=item
        return somatorio
        

class Compra:
    def __init__(self, vendedor, valor):
        self.vendedor = vendedor
        self.data = datetime.now()
        self.valor = valor      


def main():
    pessoa = Pessoa('Joao','18')
    cliente = Cliente(pessoa,'20')
    vendedor = Vendedor(pessoa,'30','200')
    compra = Compra(vendedor,28.50)
    compra2 = Compra(vendedor,30.0)
    cliente.registrar_compra(compra.valor)
    cliente.registrar_compra(compra2.valor)
    print(f'total de compras: {cliente.total_compras()}')

if 'main()' == 'main()':
    main()
   
   



