def enesima(num):
   lista = []
   while n not in lista:
       for numero in range (1,num+1):
           lista.append(numero)
           x = str(lista).strip('[]').replace(',','')
           print(x)
n = int(input('numero: '))
enesima(n)
