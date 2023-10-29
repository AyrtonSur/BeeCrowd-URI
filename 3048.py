a=int(input())
lista=[]
l=0
for n in range(0,a):
    b=int(input())
    lista.append(b)
for h in range(0,a-1):
    if lista[h]!=lista[h+1]:
        l+=1
print(l+1)
