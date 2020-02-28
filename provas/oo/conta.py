from datetime import datetime

class Historico:
    def __init__(self):
        self.data_abertura = datetime.today()
        self.transacoes = []

    def imprime(self):
        print('\nHistorico:')
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
        print(f'Dados do cliente:\nnome: {self.nome} {self.sobrenome}\nCPF: {self.cpf}\n')

        
class Conta:
    def __init__(self, numero, titular, saldo, limite, data_abertura):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.data_abertura = data_abertura
        self.historico = Historico()
        
        
        
        
    def deposita(self,valor):
        self.saldo+=valor
        self.historico.transacoes.append(f"deposito de {valor}")

    def saca(self,valor):
        if valor>self.saldo:
            return False
        else:
            self.saldo-=valor
            self.historico.transacoes.append(f"saque de: {valor}")
            
    def extrato(self,dados_cliente):
        
        print(f'Extrato da conta:\nnumero: {self.numero}\nsaldo: {self.saldo}\n')
                
        self.historico.transacoes.append(f"extrato - saldo de: {self.saldo}")
        
    def transfere_para(self,conta_destino, valor):
        sacou = self.saca(valor)
        if sacou == False:
            return False
        else:
            conta_destino.deposita(valor)
            self.historico.transacoes.append(f"transferencia de {valor} para conta {conta_destino.numero}")
            return True
    



class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano


def main():
    cliente1 = Cliente('joao','azevedo','111111111-1')
    cliente2 = Cliente('Maria','Alves','222222-2')
    data = Data("03","09","2020")
    conta1 = Conta('123-4',cliente1,1000,20000,data)
    conta2 = Conta('123-5',cliente2,1030,20000,data)
    conta1.deposita(200.0)
    conta1.saca(120.0)
    conta1.transfere_para(conta2, 300.0)
    conta1.extrato(cliente1.imprime())
    conta1.historico.imprime()
    conta2.historico.imprime()
    
    

if __name__ == '__main__':
    main()

        
    
        
