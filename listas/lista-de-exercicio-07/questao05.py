""""Crie uma classe que modele um Pokémon:
Atributos: nome, tipo, descricao, ataques, nivel, poder_luta e brilhante
Métodos: mostrar_ataques, subir_nivel, mostrar_poder_luta, e_brilhante e adicionar_ataque.

Por padrão, o atributo ataques é uma lista vazia. Com o método adicionar_ataque você deve ser 
capaz de adicionar um novo ataque à lista ataques. O método subir_nivel incrementa o atributo nível
 e o poder_luta. O atributo e_brilhante deve ser um boolean que vai indicar se o Pokémon é brilhante ou não."""

class Pokemon: 
    def __init__ (self, nome, tipo, descricao, ataques, nivel, poder_luta, brilhante = True):
        self.nome=nome
        self.tipo = tipo
        self.descricao = descricao
        self.ataques = ataques
        self.nivel = nivel
        self.poder_luta = poder_luta
        self.brilhante = brilhante

    def mostrar_ataques(self):
        print(self.ataques)

    def adicionar_ataque(self):
        self.ataques.append(self.ataques)

    def imprimir (self):
        print(f"nome: {self.nome}\ntipo: {self.tipo}\ndescriçao: {self.descricao}\nataques: {self.ataques}\nnivel: {self.nivel}\npoder: {self.poder_luta}\né brilhante? {self.brilhante}")
    

pok = Pokemon("jhoni","agua","fada",["ataque de asas","ataque de magia"],1,"voar",brilhante=False)
pok.imprimir()


