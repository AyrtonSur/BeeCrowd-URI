nome1=input()
if nome1 == 'vertebrado':
    nome2=input()
    if nome2 == 'ave':
        nome3=input()
        if nome3 == 'carnivoro':
            print('aguia')
        elif nome3 == 'onivoro':
            print('pomba')
    elif nome2 == 'mamifero':
        nome3=input()
        if nome3 == 'onivoro':
            print('homem')
        elif nome3 == 'herbivoro':
            print('vaca')
if nome1 == 'invertebrado':
    nome2=input()
    if nome2 == 'inseto':
        nome3=input()
        if nome3 == 'hematofago':
            print('pulga')
        elif nome3 == 'herbivoro':
            print('lagarta')
    if nome2 == 'anelideo':
        nome3=input()
        if nome3 == 'hematofago':
            print('sanguessuga')
        if nome3 == 'onivoro':
            print('minhoca')
