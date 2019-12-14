"""Desenvolva uma classe Macaco, que possua os atributos nome e bucho (estômago) e pelo menos 
os métodos comer, ver_bucho e digerir. Faça um programa ou teste interativamente, criando pelo
 menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo 
 do estômago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um
  macaco canibal? O método comer adiciona a comida ao atributo bucho. O método digerir remove o primeiro
   elemento do atributo bucho."""

class Macaco: 
    def __init__(self,nome,bucho):
        self.nome = nome
        self.bucho = bucho

    def comer (self,comida):
        self.bucho.append(comida)
                

    def ver_bucho(self):

        print (f'conteudo do bucho de {self.nome}: {self.bucho} ')

    def digerir(self):
        del(self.bucho[0])

    def imprimir (self):
        print(f'digerido: {self.bucho}')


macaco = Macaco("chico",['banana','morango','maça'])
macaco.comer('uva)
macaco.ver_bucho()
macaco.digerir()
macaco.imprimir()

macaco2 = Macaco("zé",['banana','milho','feijoada'])
macaco2.comer(macaco)
macaco2.ver_bucho()
macaco2.digerir()
macaco2.imprimir()