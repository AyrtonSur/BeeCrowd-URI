while True:
    try:
        a,b=map(int, input().split())
        matriz=[]
        for n in range(a):
            linha=list(map(int, input().split()))
            matriz.append(linha)
        for n in range(a):
            if sum(matriz[n])==2:
                g=matriz[n].index(2)
                k=n
            elif sum(matriz[n])==3:
                g=matriz[n].index(2)
                k=n
                l=matriz[n].index(1)
                p=n
            elif sum(matriz[n])==1:
                l=matriz[n].index(1)
                p=n
        x1=max(g,l)
        x2=min(g,l)
        y1=max(k,p)
        y2=min(k,p)
        lol=(x1-x2)+(y1-y2)
        print(lol)
    except EOFError:
        break
