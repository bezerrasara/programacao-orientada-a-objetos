def cria_conta(numero,titular,saldo,limite):
    ''' descrição:
            esta funçao cria e retorna uma conta.
            
        parametros:
            numero - numero da conta.
            titular - nome do cliente.
            saldo - valor disponivel.
            limite - limite do saque.'''
            
            
    
    conta = {"numero":numero,"titular":titular,"saldo":saldo,"limite":limite}
    return conta
#print(cria_conta.__doc__)

def deposita(conta, valor):
    ''' descricao:
            Esta funcao adiciona um valor na conta.
        parametros:
            conta - acessa a chave 'saldo' em conta(dicionario).
            valor - eh adicionado em conta.
            
        '''
    conta['saldo']+=valor

def saca(conta,valor):
    '''descricao:
        esta funcao retira um valor da conta.'''
    conta['saldo']-=valor

def extrato(conta):
    '''descricao:
        esta funcao mostra os dados da conta'''
    
    print(f'conta: {conta["numero"]}\nsaldo: {conta["saldo"]}')
