peso = float(input ('peso: '))
if peso > 50:
    excesso = peso - 50
    multa = 4*excesso
    print (f'Kg além do limite: {excesso}')
    print (f'Sua multa é de: R$ {multa:.2f}')
else:
    print ('Peso dentro do limite.')
   
    