N1 = float (input('N1: '))
N2 = float (input('N2: '))
media = (N1+N2)/2
if media>=7 and media <10:
    print('Aprovado.')
elif media <7:
    print ('Reprovado.')
elif media == 10:
    print ('Aprovado com distinção')