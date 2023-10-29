a=int(input())
lista1=list(map(int, input().split()))
lista2=[]
u=0
l=0
for n in range(0,a-1):
    g=lista1[n+1]-lista1[n]
    if g>0:
        lista2.append('pico')
    elif g<0:
        lista2.append('vale')
    elif g==0:
        u=1
        break
d=len(lista2)
if u==0 and d>1:
    z=lista2[0]
    m=lista2[1]
    if u==0 and m!=z:
        for g in range(0,d-1):
            if lista2[g]==lista2[g+1]:
                l+=1
        if l==0:
            print(1)
        else:
            print(0)
    else:
        print(0)
elif d==1 and u==0:
    print(1)
else:
    print(0)
