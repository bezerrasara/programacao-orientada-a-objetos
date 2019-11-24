def converter(hora,minuto):
    
    if hora > 12 and hora <24:
        h = hora - 12
        print(f'{h}:{minuto} P.M.')
    elif hora == 12:
        h =12
        print(f'{h}:{minuto} P.M.')
    elif hora == 24:
        h = hora - 12
        print(f'{h}:{minuto} A.M.')
    else:
        print(f'{hora}:{minuto} A.M.')

def saida(A,P):
    converter(A,P)
   
    
while True:
    h = int(input('Hora: '))
    min = int(input('Minutos: '))
    saida (h,min)
    continuar = input('Deseja continuar? (S/N)')
    if continuar in 'Nn':
        break
    
