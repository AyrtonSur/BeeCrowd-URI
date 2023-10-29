e=int(input())
lista1=[]
lista2=[]
for n in range(0,e):
    z=int(input())
    if z%2==0:
        lista1.append(z)
    elif z%2==1:
        lista2.append(z)
lista1.sort()
lista2.sort(reverse=True)
lista3=lista1+lista2
g=len(lista3)
for h in range(0,g):
    print(lista3[h])
