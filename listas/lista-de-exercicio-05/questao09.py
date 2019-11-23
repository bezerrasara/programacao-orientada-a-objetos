def reverso(numero):
    reverso = numero[::-1]
    return reverso


n = input("digite um numero: ")
rev = reverso(n)
print(f'reverso do numero: {rev}')

