from random import randint
from time import sleep


print('---JOGO DE CRAPS---')
def jogo_craps(jogo): 
    while jogo == 'jogando o dado!':
        dados = randint(2,12)
        print(dados)
        if dados == 7 or dados==11:
            print('Voce é um jogador Natural!!!\nPARABENS!!!')
            break
                            
        elif dados == 2 or dados ==3 or dados == 12:
            print('CRAPS:(\nVoce perdeu!')
            break
        
        if dados == 4 or dados == 5 or dados ==6 or dados==8 or dados == 9 or dados ==10:
            cont = 0
            cont += dados
            print('Este é seu ponto, seu objetivo é jogar os dados ate tirar esse numero novamente!!')
            
            print(jogo)
             
            sleep(0.5)
            continue
            if cont != dados:
                break

jogada = 'jogando o dado!'
x = jogo_craps(jogada)







