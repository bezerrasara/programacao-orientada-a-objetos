from random import randint
from random import uniform
n = int(input())
lista = ['Amanda','Bruna','Carlos','Daniel','Evandro','Guilherme','Henrique','Inacio','João','Kelly','Leandro','Marcos','Nadia','Olivia','Paulo','Renata','Sabrina','Tatiana','Ulyssis','Vanessa']
lista2 = ['Santos','da Silva','Alves','Moreira','Figueredo','Martins','Amorim','Rodrigues','Bitencout','Barbosa','Ferreira','Gonçalves','Oliveira','Coutinho','Pereira','Sousa','Muniz','Morais','Duarte','Gomes']



with open ('pessoas.txt','w') as arquivo:
    for nomes in range(1,n+1):
        nome = randint(0,len(lista)-1)
        sobrenome = randint(0,len(lista)-1)
        idade = randint(0,101)
        altura = uniform(1.30,1.90)
        print(f'{lista[nome]} {lista2[sobrenome]}, {idade}, {altura:.2f}',file=arquivo)





