def copia_arquivo(nome1,nome2):

    with open(nome1) as arquivo1:
        with open(nome2, 'w') as arquivo2:
            for linha in arquivo1:
                if '//' not in linha:
                    print(linha, file = arquivo2)
copia_arquivo("frase.txt","frase_copiada.txt")    