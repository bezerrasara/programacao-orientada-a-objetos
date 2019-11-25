from random import randint
n = int (input())
matriz = list()
for i in range (n):
    randint(1,9)
    matriz.append(list().split())
lista = []
for i in range(n):
    soma = 0
    for j in range(n):
        soma += matriz[i][j]
lista.append()

for j in range(n):
    soma = 0
    for i in range(n):
        soma += matriz[i][j]
lista.append()

soma = 0
for i in range(n):
    soma+=matriz[i][i]
lista.append(soma)

soma = 0
i =0
j = n-1
while i < n:
    soma += matriz[i][j]
    i+=1
    j-=1
lista.append(soma)

magico = True
index = 0
while magico and index < len(lista):
    if lista [index]!=lista[0]:
        magico == False
    index += 1
if magico :
    print('magico')
else:
    print('nao')