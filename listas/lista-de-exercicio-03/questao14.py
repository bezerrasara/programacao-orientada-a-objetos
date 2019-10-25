
n1 = float(input('N1: '))
n2 = float(input('N1: '))
media = (n1+n2)/2
if media >=9 and media<=10:
  print(f'notas: {n1}, {n2}')
  print(f'media: {media}')
  print('conceito: A')
  print('APROVADO')
if media >=7.5 and media<=9:
  print(f'notas: {n1}, {n2}')
  print(f'media: {media}')
  print('conceito: B')
  print('APROVADO')
if media >=6 and media<=7.5:
  print(f'notas: {n1}, {n2}')
  print(f'media: {media}')
  print('conceito: C')
  print('APROVADO')
if media >=4 and media<=6:
  print(f'notas: {n1}, {n2}')
  print(f'media: {media}')
  print('conceito: D')
  print('REPROVADO')
if media >=0 and media<=4:
  print(f'notas: {n1}, {n2}')
  print(f'media: {media}')
  print('conceito: E')
  print('REPROVADO')

