"""Crie uma classe que modele um Tamagotchi (Bichinho Eletrônico):
Atributos: nome, fome, saude, idade.
Métodos: alterar_nome, retornar_fome, retornar_saúde, retornar_idade, comer, tomar_injecao e envelhecer.

Os atributos fome e saúde iniciam, por padrão, com 10. O atributo idade inicia, por padrão, com 0.

O método comer incrementa o atributo fome em uma unidade (até o máximo 10). O método tomar_injeção 
incrementa o atributo saude em uma unidade (até o máximo 10). O método envelhecer decrementa os atributos
 saude e idade em uma unidade (até o mínimo 0) e incrementa o atributo idade em uma unidade (sem limite)."""
 
class Tamagotchi:
    def __init__(self,nome="Ana",fome=10,saude=10,idade=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self,novo_nome):
        self.nome = novo_nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def comer (self):
        for comida in range(self.fome):
            self.fome+=1

    def tomar_injecao(self):
        for injecao in range(self.saude):
            self.saude+=1

    def envelhecer(self):
        self.saude-=1
        self.idade+=1

    def imprimir (self):
        print(f'nome: {self.nome}\nfome: {self.fome}\nsaude: {self.saude}\nidade: {self.idade}')


tamagotchi = Tamagotchi()
tamagotchi.alterar_nome(input("novo nome: "))
tamagotchi.retornar_fome()
tamagotchi.retornar_idade()
tamagotchi.retornar_saude()
tamagotchi.comer()
tamagotchi.tomar_injecao
tamagotchi.envelhecer()
tamagotchi.imprimir()
