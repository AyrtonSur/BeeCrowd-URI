x=int(input())
lista1=[]
for n in range(0,x):
    d=int(input())
    lista1.append(d)
lista2=lista1
lista2.sort()
lista3=[]
[lista3.append(item) for item in lista2 if item not in lista3]
lista4=[]
for h in lista3:
    k=lista2.count(h)
    print(f'{h} aparece {k} vez(es)')
