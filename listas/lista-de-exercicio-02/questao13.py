altura = float (input ('Altura: '))
sexo = input ('sexo (M/F): ')
if sexo in 'mM':
    peso_idM = (72.7*altura)-58
    print (f'seu peso ideal é: {peso_idM:.2f}')
elif sexo in 'fF':
    peso_idF = (62.1*altura)-44.7
    print (f'seu peso ideal é: {peso_idF:.2f}')