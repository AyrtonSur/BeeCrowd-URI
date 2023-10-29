a,b,c=map(int, input().split())
lista=list(map(int, input().split()))
l=0
lista2=[]
k=0
for n in range(0+k,a-1):
    for g in range(1+k,a):
        f=lista[n]+lista[g]
        lista2.append(f)
    k+=1
d=len(lista2)
for h in range(d):
    if lista2[h] in range(b,c+1):
        l+=1
print(l)
