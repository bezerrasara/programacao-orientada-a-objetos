n1 = float (input ('produto1: '))
n2 = float (input ('produto2: '))
n3 = float (input ('ptoduto3: '))
if n1<n2 and n1<n3:
    print(f'comprar: produto1 {n1:.2f}')
elif n2<n3 and n2<n3:
    print(f'comprar: produto2 {n2:.2f}')
else:
    print (f'comprar: produto3 {n3:.2f}')