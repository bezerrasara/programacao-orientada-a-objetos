
def conversao(numero):
    calculo = float(numero/(1024*1024))
    return calculo


def calculo_de_percentual(usuario,total):
    percentual = (usuario[2]/total)*100
    usuario.append('{:.2f}%'.format(percentual))
    
    

usuarios = []
total = 0
media = 0
posicao = 1

with open("usuarios.txt","r") as arquivo:
    for linha in arquivo:
        usuarios.append(linha.split())

    for usuario in usuarios:        
        usuario.insert(0,posicao)
        usuario[2] = conversao(float(usuario[2]))
        total += usuario[2]
        posicao += 1

    for usuario in usuarios:
        calculo_de_percentual(usuario,total)

    media = total/len(usuarios)


with open("relatorio.txt","w") as arquivo:
    with open("relatorio.txt","w") as dados:
        print(f"ACME Inc.           Uso do espaco em disco pelos usuarios\n{'-'*65}",file=dados)
        print("Nr.      Usuario       Espaco Utilizado          % do uso\n",file=dados)
        for usuario in usuarios:
            print(f'{usuario[0]} {usuario[1]:>15}',end=' ',file=dados)   
            print(f'{float(usuario[2]):>20.2f}MB {(usuario[3]):>15}',file=dados)
               
        
        print(f'\nEspaco total ocupado: {total:.2f} MB',file=dados)
        print(f'Espaco medio ocupado: {media:.2f} MB',file=dados)
            

    
