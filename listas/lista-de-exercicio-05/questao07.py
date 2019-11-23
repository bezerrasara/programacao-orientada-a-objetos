cont = 0
soma = 0
def valor_pagamento(valor,dias):
    if dias > 0:
        v = valor+(valor*(3/100))+((0.1/100)*dias)
        return v
    else:
        print(valor)
    
def saida(mensagem):
    print ('_'*len(mensagem))
    print (mensagem)
    print ('_'*len(mensagem))

while True:
    prestacao = float(input('valor da prestacao: '))
    cont+=1
    if prestacao == 0:
        break
    dias = int(input('Quantidade de dias atrasados: '))
    x = valor_pagamento(prestacao,dias)
    print ('valor a ser pago: {:.2f}'.format(x))

    soma+=x
msgm = 'RELATORIO DIARIO'
A = saida(msgm)
print ('Quantidade de prestações pagas: {}\nTotal pago: {:.2f}'.format(cont-1,soma))
    