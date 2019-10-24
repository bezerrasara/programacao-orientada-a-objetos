ganho_hora = float (input ('Ganho por hora: '))
horas = float (input ('Horas trabalhadas no mês: '))
salarioB = ganho_hora*horas
IR = (salarioB*(11/100))
INSS = (salarioB*(8/100))
sind = (salarioB*(5/100))
descontos = salarioB-(salarioB*(8/100))-(salarioB*(8/100))-(salarioB*(5/100))

print (f'Salario bruto: R$ {salarioB:.2f}')
print (f'IR: R$ {IR:.2f}')
print (f'INSS: R$ {salarioB*8/100:.2f}')
print (f'Sindicato: R$ {salarioB*5/100:.2f}')
print (f'Salário Liquido: R$ {descontos:.2f}')