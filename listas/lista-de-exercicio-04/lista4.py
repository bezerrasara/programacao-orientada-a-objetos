Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0
arq = open("amazon.csv")
dados = arq.read()
for linha in dados.splitlines():
	linha = linha.strip(' ')
	ano, cidade, mes, casos, data = linha.split(',')
	casos= casos.replace(".", "")
		
	if '"Acre"' == cidade and ano == '2015':
		Q1 += int(casos)


	elif '"Ceara"' == cidade and ano == '2014':
		Q2 += int(casos)

		
	elif '"Amazonas"' == cidade:
		Q3 += int(casos)

		
		
	elif ano == '"year"':
		continue

	elif int(ano) >= 2010 and cidade == '"Mato Grosso"':
		Q4 += int(casos)



print('~'*20)
print ('     RESPOSTAS:')
print('~'*20)
print(f'QUESTÃO 1 : {Q1}')
print(f'QUESTÃO 2 : {Q2}')
print(f'QUESTÃO 3 : {Q3}')
print(f'QUESTÃO 4 : {Q4}')


		

arq.close()
	#print('ARQUIVO FECHADO')