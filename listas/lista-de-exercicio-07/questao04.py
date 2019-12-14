"""Crie uma classe que modele uma caneta:
Atributos: cor, marca, numero_ponta, volume_tinta
Métodos: encher_caneta, escrever, retornar_marca e imprimir_caracteristicas

Por padrão, o atributo volume_tinta sempre começa com o inteiro 50. O método 
escrever irá imprimir na tela uma string passada para o método e decrementar 
o volume_tinta em uma unidade (representando a tinta gasta ao escrever).
 O método encher_caneta aumenta o volume_tinta para 50 novamente."""

class Caneta:
    def __init__(self,cor,marca,numero_ponta,volume_tinta):
        self.cor = cor
        self.marca = marca
        self.numero_ponta = numero_ponta
        self.volume_tinta = volume_tinta

    def encher_caneta(self ):
        self.volume_tinta = 50
        

    def escrever (self, palavra):
        print(palavra)
        self.volume_tinta -=1

    def retornar_marca(self):
        return self.marca

    def imprimir (self):
        print(f"{self.cor}, {self.marca}, {self.numero_ponta}, {self.volume_tinta}")

c1 = Caneta("Azul", "bic", 0.7, 50)
c1.escrever("Azul caneta")
c1.imprimir()






