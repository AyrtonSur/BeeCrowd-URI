while True:
    try:
        a=int(input())
        lista1=[]
        g=0
        for n in range(a):
            b=str(input())
            lista1.append(b)
        lista1.sort()
        d = list(lista1[n])
        p=len(d)
        for n in range(a-1):
            d=list(lista1[n])
            c=list(lista1[n+1])
            for k in range(p):
                if d[k]==c[k]:
                    g+=1
                else:
                    break
        print(g)
    except EOFError:
        break
