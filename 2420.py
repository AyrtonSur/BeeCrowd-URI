a=int(input())
lista=list(map(int,input().split()))
tamanho=sum(lista)/2
c=lista[0]
d=lista[-1]
l=0
g=0
while c!=tamanho or d!=tamanho:
    if c!=tamanho:
        l+=1
        c+=lista[l]
    if d!=tamanho:
        g+=1
        d+=lista[-g-1]
print(l+1)
