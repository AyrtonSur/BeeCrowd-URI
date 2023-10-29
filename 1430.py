dic={'W':1,'H':0.5,'Q':0.25,'E':0.125,'S':0.0625,'T':0.03125,'X':0.015625}
letras=[True]
while letras[0]!='*':
    l=0
    letras=list(map(str,input().split('/')))
    if letras[0]!='*':
        for n in range(1,len(letras)-1):
            e=0
            compasso=list(letras[n])
            for n in range(len(compasso)):
                e+=dic[compasso[n]]
            if e==1:
                l+=1
        print(l)
    else:
        break
