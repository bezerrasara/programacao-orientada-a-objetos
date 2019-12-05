def media(arq1, arq2):
    
    with open(arq1) as arquivo1:
        with open(arq2) as arquivo2:
            with open("arquivo_gerado.txt","w") as arquivo3:

                for linha in arquivo1:
                    print(linha,file=arquivo3,end='')
                    for linha2 in arquivo2:
                        
                        linha2 = linha2.split()
                        for nota in linha2:
                    
                            
                        
                            print(f'{linha2} ',file=arquivo3,end='')


media("alunas.txt","notas.txt")