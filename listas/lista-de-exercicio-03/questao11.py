salario = float (input ('salario atual: '))
if salario <= 280:
    R = salario+(salario*(20/100))
    print (f'salario atual: {salario}')
    print ('percentual aplicado: 20%')
    print (f'valor do aumento: {salario*(20/100)}')
    print (f'salario com reajuste: {R}')
elif salario >280 and salario <700:
    print (f'salario atual: {salario}')
    print ('percentual aplicado: 15%')
    print (f'valor do aumento: {salario*(15/100)}')
    R = salario+(salario*(15/100))
    print (f'salario com reajuste: {R}')
elif salario >700 and salario <1500:
    print (f'salario atual: {salario}')
    print ('percentual aplicado: 10%')
    print (f'valor do aumento: {salario*(10/100)}')
    R = salario+(salario*(10/100))
    print(f'salario com reajuste: {R}')
elif salario >=1500:
    print (f'salario atual: {salario}')
    print ('percentual aplicado: 5%')
    print (f'valor do aumento: {salario*(5/100)}')
    R = salario+(salario*(5/100))
    print (f'salario com reajuste: {R}')