a=int(input())
lista=list(map(int, input().split()))
l=0
for n in range(0,a-1):
    if lista[n]<=lista[n+1]:
        l+=0
    elif lista[n]>lista[n+1]:
        l+=1
        g=n+2
        break
if l==0:
    print(0)
else:
    print(g)
