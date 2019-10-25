lado1, lado2, lado3 = input('lado1: ').split()
lado1=float(lado1)
lado2=float(lado2)
lado3=float(lado3)
if lado1+lado2>lado3 or lado1+lado3>lado2 or lado2+lado3>lado1:
  print('formam um triangulo')
  if lado1==lado2 and lado1==lado3:
    print ('triangulo equilatero')
  elif lado1==lado2 or lado2==lado3 or lado1==lado3:
    print('triangulo isósceles')
  if lado1!=lado2 and lado2!=lado3 and lado1!=lado3:
    print('triangulo escaleno')