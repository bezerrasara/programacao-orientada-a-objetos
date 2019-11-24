def mesPorExtenso(dia,mes,ano):
    meses = (0,'janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro')
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    if  mes<=12 and mes >=1: 
        print (f'{dia} de {meses[mes]} de {ano}')
    else:
        print('NULL')

dia,mes,ano = input('data: ').split('/')
mesPorExtenso(dia,mes,ano)
