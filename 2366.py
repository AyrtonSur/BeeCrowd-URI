a, b = map(int, input().split())
lista = list(map(int, input().split()))
lista.append(42195)
l=0
for n in range(a):
    if lista[n+1]-lista[n]<=b:
        l+=1
    else:
        l-=1
if l==a:
    print('S')
else:
    print('N')
