from random import randint
from time import sleep
jogo = 0

print('---JOGO DE CRAPS---')
#primeira jogada 
while True:
    jogada = int(input('digite 1 para jogar o dado: '))
    sleep(0.5)
    jogo +=1
    while jogo==1:
        dados = randint(2,12)
        print(dados)
        if dados == 7 or dados==11:
            print('Voce é um jogador Natural!!!\nPARABENS!!!')
            print(dados)
                            
        elif dados == 2 or dados ==3 or dados == 12:
            print(dados)
            print('CRAPS:(\nVoce perdeu!')
        else:
            print(dados)
            break
        
        if dados == 4 or dados == 5 or dados ==6 or dados==8 or dados == 9 or dados ==10:
            jogo+=1
            print('Este é seu ponto, seu objetivo é jogar os dados ate tirar esse numero novamente!!')
            print(dados)

    while jogo == 2:
        if dados == 7:
            print('voce perdeu')
            print(dados)
            
        else:
            print(dados)
            break

            continue
