from datetime import datetime

class Historico:
    def __init__(self):
        self.data_abertura = datetime.today()
        self.transacoes = []

    def imprime(self):
        print(f'data de abertura: {self.data_abertura}')
        if self.transacoes: 
            print('transacoes: ')
            for t in self.transacoes:
                print('-', t)
        else:
            print('não houve transacoes nesta conta')

class Cliente:
    def __init__(self,nome,sobrenome,cpf):
        self.nome = nome
        self.sobrenome= sobrenome    
        self.cpf = cpf
    def imprime(self):
        print(f'nome: {self.nome} {self.sobrenome}\nCPF: {self.cpf}')
        
class Conta:
    def __init__(self, numero, titular, saldo, limite, data_abertura):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.data_abertura = data_abertura
        self.historico = Historico()
        self.cliente = Cliente.imprime
        
        
        
    def deposita(self,valor):
        self.saldo+=valor
        self.historico.transacoes.append(f"deposito de {valor}")

    def saca(self,valor):
        if valor>self.saldo:
            return False
        else:
            self.saldo-=valor
            self.historico.transacoes.append(f"saque de: {valor}")
            
    def extrato(self):
        print(f'numero: {self.numero}\nsaldo: {self.saldo}\n{self.cliente()}')
        self.historico.transacoes.append(f"extrato - saldo de: {self.saldo}")
        
    def transfere_para(self,conta_destino, valor):
        sacou = self.saca(valor)
        if sacou == False:
            return False
        else:
            conta_destino.deposita(valor)
            self.historico.transacoes.append(f"transferencia de {valor} para conta {conta_destino.numero}")
            return True
    

"""class Cliente(Conta):
    def __init__(self,nome,sobrenome,cpf):
        self.nome = nome
        self.sobrenome= sobrenome    
        self.cpf = cpf

    #def imprime(self):
       # print(f'nome: {self.nome} {self.sobrenome}\nCPF: {self.cpf}')"""

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        
        
    
        
