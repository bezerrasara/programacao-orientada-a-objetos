"""Baseado nas questões implementadas, proponha 5 questões para exercitar 
a modelagem de objetos da vida real. Seja criativo e utilize exemplo do seu cotidiano, hobbies, etc.

Suas questões devem solicitar uma solução com atributos e métodos. Às questões também devem abordar
 o tema atributo padrão em um construtor. Os métodos devem interagir com os atributos quando forem chamados,
  com verificações dos atributos."""
from time import sleep
class Carro:
    def __init__(self,cor,rodas,marca,tanque):
        self.cor = cor
        self.rodas = rodas
        self.marca  = marca
        self.tanque = tanque
    
    def abastecer(self, litros):
        if self.tanque + litros > 50:
            print("Abastecendo tanque...")
            sleep(1)
            print("Erro! o tanque ja esta cheio.\n")
        else:
            self.tanque+=litros
            print("Abastecendo tanque...")
            sleep(1)
            print(f'tanque abastecido: {self.tanque}\n')
        
    def print(self):
        print(f'cor: {self.cor}\nrodas: {self.rodas}\nmarca: {self.marca}\ntanque: {self.tanque} litros')

carro_azul = Carro('azul',4, 'BMW',30 )
print("carro")
carro_azul.print()
carro_azul.abastecer(50)