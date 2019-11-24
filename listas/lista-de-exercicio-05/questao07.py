
def valor_pagamento(valor,dias):
    if dias > 0:
        v = valor+(valor*(3/100))+((0.1/100)*dias)
        print ('valor com juros: ',v)       
    elif dias == 0:
        print('valor sem juros',valor)
        
cont = 0
soma = 0       
while True:
    prestacao = float(input('valor da prestacao: '))
    cont+=1
    soma+=prestacao
    if prestacao== 0:
        print ('Quantidade de prestações pagas: {}\nTotal pago: {:.2f}'.format(cont-1,soma))
        break
    dias = int(input('Quantidade de dias atrasados: '))
    x = valor_pagamento(prestacao,dias)
    
    