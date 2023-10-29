a=int(input())
lista1=[]
for n in range(a):
    lista=list(map(str, input().split()))
    lista2=sorted(lista, key=len, reverse=True)
    lista1.append(lista2)
for n in range(len(lista1)):
    print(' '.join(lista1[n]))
