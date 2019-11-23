def soma(n1,n2,n3):
    soma=n1+n2+n3
    return(soma)
    
num1,num2,num3 = input('digite 3 numeros: ').split()
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
a = soma(num1,num2,num3)
print (f'{num1} + {num2} + {num3} = {a}')