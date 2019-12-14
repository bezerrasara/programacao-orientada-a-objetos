"""Questão 07
Crie uma classe que modele uma pessoa:
Atributos: nome, idade, peso e altura
Métodos: envelhecer, engordar, emagrecer e crescer

Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm."""

class Pessoa:
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade+=1

    def engordar(self):
        self.peso+=2

    def emagrecer(self):
        self.peso-=2

    def crescer(self):
        if self.idade<21:
            self.altura += 0.05
        else:
            print(f"altura: {altura}")
    
    def imprimir(self):
        print(f'nome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}\nAltura: {self.altura}')


pessoa = Pessoa("Fernando",20,79,1.50)
pessoa.crescer()
pessoa.emagrecer()
pessoa.engordar()
pessoa.imprimir()