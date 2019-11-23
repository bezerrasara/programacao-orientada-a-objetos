
import random
def embaralha(palavra):
    embaralha = list(palavra)
    random.shuffle(embaralha)
    embaralha = "".join(embaralha)

    embaralha = "".join(random.sample(palavra, len(palavra)))
    print (embaralha)


x = embaralha('vida')