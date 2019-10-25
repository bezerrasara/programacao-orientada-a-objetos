valor_hora=float(input("Informe o valor da hora trabalhada: "))
hora=int(input("Informe a quantidade de horas trabalhadas: "))

salario=valor_hora*hora

if (salario<=900):
    inss=(salario*10)/100
    fgts=(salario*11)/100
    sindicato=(salario*3)/100
    desconto=inss+sindicato
    salario_liquido=salario-desconto
    print("Salário Bruto: R$",salario)
    print("IR: Isento")
    print("INSS: R$",inss)
    print("FGTS: R$",fgts)
    print("Total de Descontos: R$",desconto)
    print("Salário Liquido: R$",salario_liquido)
elif(salario<=1500):
    ir=(salario*5)/100
    inss=(salario*10)/100
    fgts=(salario*11)/100
    sindicato=(salario*3)/100
    desconto=inss+sindicato
    salario_liquido=salario-desconto
    print("Salário Bruto: R$",salario)
    print("IR: R$",ir)
    print("INSS: R$",inss)
    print("FGTS: R$",fgts)
    print("Total de Descontos: R$",desconto)
    print("Salário Liquido: R$",salario_liquido)
elif(salario<=2500):
    ir=(salario*10)/100
    inss=(salario*10)/100
    fgts=(salario*11)/100
    sindicato=(salario*3)/100
    desconto=inss+sindicato
    salario_liquido=salario-desconto
    print("Salário Bruto: R$",salario)
    print("IR: R$",ir)
    print("INSS: R$",inss)
    print("FGTS: R$",fgts)
    print("Total de Descontos: R$",desconto)
    print("Salário Liquido: R$",salario_liquido)
else:
    ir=(salario*20)/100
    inss=(salario*10)/100
    fgts=(salario*11)/100
    sindicato=(salario*3)/100
    desconto=inss+sindicato
    salario_liquido=salario-desconto
    print("Salário Bruto: R$",salario)
    print("IR: R$",ir)
    print("INSS: R$",inss)
    print("FGTS: R$",fgts)
    print("Total de Descontos: R$",desconto)
    print("Salário Liquido: R$",salario_liquido)