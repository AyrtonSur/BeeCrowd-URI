a=True
while a!=0:
    a=int(input())
    lista2=[]
    lista3=[]
    w=0
    z=0
    if a!=0:
        lista=list(map(int, input().split()))
        lista.sort(reverse=True)
        for n in range(2):
            lista1=[]
            for h in range(a):
                k=lista[h+(a*n)]
                lista1.append(k)
            lista2.append(lista1)
        for n in range(a):
            j=lista2[0][n]+lista2[1][-1-n]
            lista3.append(j)
        print(max(lista3),min(lista3))
    else:
        break
