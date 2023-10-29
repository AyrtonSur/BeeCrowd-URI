a=int(input())
for n in range(a):
    dieta=input().upper()
    café=input().upper()
    almoço=input().upper()
    comida=almoço+café
    for h in range(len(comida)):
        if comida[h] not in dieta:
            dieta='CHEATER'
            break
        else:
            dieta = dieta.replace(comida[h], '')

    if dieta != 'CHEATER':
        dieta = ''.join(sorted(dieta))
    print(dieta)
