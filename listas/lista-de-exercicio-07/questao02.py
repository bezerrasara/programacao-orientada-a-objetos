"""O atributo componentes deve ser uma lista que vai conter componentes de um computador (use o tipo string).
 Por exemplo, ['monitor', 'teclado', 'mouse'].
O método adicionarComponentes vai adicionar um novo componente à lista de componentes já existente.
O método mostrar_anos_uso vai mostrar quantos anos de uso o computador possui. Se for menor do que 6, 
imprima a quantidade de anos de uso. Se for maior ou igual a 6, imprima a frase: "Seu computador está
 tão velho que tem problemas de junta… junta tudo e joga fora...".
O método envelhecer incrementa o atributo anos_uso.
"""

class Computador:
    def __init__(self,marca,modelo,componentes,anos_uso,cor):
        self.marca=marca
        self.modelo = modelo
        self.componentes = componentes
        self.anos_uso = anos_uso
        self.cor = cor

    def mostrarMarca(self):
        print(self.marca)

    def adicionarComponentes(self,novosComponentes):
        self.componentes.append(novosComponentes)

    def mostrar_anos_uso(self):
        if self.anos_uso > 6:
            print("Seu computador está tão velho que tem problemas de junta… junta tudo e joga fora...")
        else:
            print(f'anos de uso: {self.anos_uso}')


    def envelhecer(self):
        self.anos_uso+=1

    def imprimir(self):
        print(f'marca: {self.marca}\nmodelo: {self.modelo}\ncomponentes: {self.componentes}\nanos de uso(incrementado): {self.anos_uso}\ncor: {self.cor}')


computador = Computador("samsung","padrao",["teclado","mouse","monitor"],5,"preto")

computador.adicionarComponentes("cabo")
computador.mostrar_anos_uso()
computador.envelhecer()
computador.imprimir()