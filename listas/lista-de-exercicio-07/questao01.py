"""Crie uma classe que modele uma bola:
Atributos: cor, circunferência, material
Métodos: trocaCor e mostraCor"""

class Bola:
    def __init__(self,cor,circunferencia,material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material =material

    def trocaCor(self,novaCor):
        self.cor = novaCor

    def mostraCor(self):
        print(f'cor antiga: {self.cor}')

    def imprimir(self):
        print(f'nova cor: {self.cor}\ncircunferencia: {self.circunferencia}\nmaterial: {self.material}')

bola = Bola("azul",4,"coro")
bola.mostraCor()
bola.trocaCor("roza")
bola.imprimir()

