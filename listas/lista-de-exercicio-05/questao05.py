def somaImposto(taxaImposto, custo):
    alteracusto = custo + (taxaImposto/100)*custo
    return alteracusto


imposto = float(input('porcentagem do imposto: '))
produto = float(input('produto: '))
x = somaImposto(imposto, produto)
print(f'valor após imposto: R$ {x}')

