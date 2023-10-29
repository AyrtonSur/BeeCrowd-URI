a=int(input())
for n in range(a):
    lista=[]
    b=int(input())
    nomes=list(map(str, input().split()))
    faltas=list(map(str, input().upper().split()))
    for n in range(len(nomes)):
        p=0
        boc=list(faltas[n])
        doc=len(boc)
        for h in range(len(boc)):
            if boc[h]=='P':
                p+=1
            elif boc[h]=='M':
                doc-=1
            else:
                p+=0
        if p/doc<0.75:
            lista.append(nomes[n])
    print(' '.join(lista))
