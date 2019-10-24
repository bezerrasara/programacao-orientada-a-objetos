n1 = int (input ('numero1: '))
n2 = int (input ('numero2: '))
n3 = int (input ('numero3: '))
if n1>n2 and n1>n3 and n2>n3:
    print(f'maior: {n1}')
    print(f'menor: {n3}')
elif n1>n2 and n1>n3 and n3>n2:
    print (f'maior: {n1}')
    print (f'menor: {n2}')
elif n2>n3 and n2>n1 and n1>n3:
    print(f'maior: {n2}')
    print(f'menor: {n3}')
elif n2>n3 and n2>n1 and n3>n1:
    print(f'maior: {n2}')
    print(f'menor: {n1}')
elif n3>n1 and n3>n2 and n2>n1:
    print (f'maior: {n3}')
    print (f'menor: {n1}')
elif n3>n1 and n3>n2 and n1>n2:
    print (f'maior: {n3}')
    print (f'menor: {n2}')