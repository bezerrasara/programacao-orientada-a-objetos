def cria_conta(numero,titular,saldo,limite):
    conta = {"numero":numero,"titular":titular,"saldo":saldo,"limite":limite}
    return conta

def deposita(conta, valor):
    conta['saldo']+=valor

def saca(conta,valor):
    conta['saldo']-=valor

def saldo(conta):
    print(f'conta: {conta['numero']}\nsaldo: {conta['saldo']}')