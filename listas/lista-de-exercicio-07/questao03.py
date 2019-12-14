"""Crie uma classe que modele um quadrado:
Atributos: Tamanho do lado
Métodos: mudar_valor_lado, retornar_valor_lado e calcular_area"""
class Quadrado:
    def __init__(self,lado):
        self.lado = lado

    def mudar_valor_lado(self,novo_lado):
        self.lado = novo_lado

    def retornar_valor_lado(self):
        return self.lado

    def calcular_area(self):
        return self.lado*self.lado
        
    def imprimir (self):
        print(f'Tamanho do lado: {self.lado}')

q1 = Quadrado(15)
q1.mudar_valor_lado(20)
x = q1.calcular_area()
q1.imprimir()
print(f'area = {x}\n')

