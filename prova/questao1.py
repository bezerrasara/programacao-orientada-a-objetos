def converte (bytes):
    mb = bytes*(9537*(10**-7))
    print(f'{mb:.2f} MB')


def percentual (total,mb):
    p=total*(mb/100)
    print(f'{p:.2f}%') 

print("__main__")
with open("usuarios.txt") as arquivo:
    with open ("relatorio.txt","w") as arquivo2:
        for linha in arquivo.splitlines():
            
            print(f'{linha}',file=arquivo2)



            