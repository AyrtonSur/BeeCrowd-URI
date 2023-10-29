f1 = 1
f2 = 1
l=0
lista1=[]
lista2=[]
lista1.append(f1)
lista1.append(f2)
for n in range(0,25):
    fn=f1+f2
    f2=f1
    f1=fn
    lista1.append(fn)
for h in range(1,200000):
    for p in range(0,25):
        if h!=lista1[p]:
            l+=1
        elif h==lista1[p]:
            l+=0
    if l==25:
        lista2.append(h)
    l=0
g=int(input())-1
d=lista2[g]
print(d)

#this is probably my worst working code in the entire list and there is a chance it won't work in your pc because of the loading time
