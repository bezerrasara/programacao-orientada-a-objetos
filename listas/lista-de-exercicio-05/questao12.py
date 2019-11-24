
import random
def embaralha(palavra):
    embaralha = list(palavra)
   

    embaralha = "".join(random.sample(palavra, len(palavra)))
    print (embaralha)


x = embaralha(input('digite uma palavra: '))
