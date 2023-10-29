a=int(input())
lista=[]
for n in range(a):
    a,b=map(float, input().split())
    c=a*(1000/b)
    lista.append(c)
d=min(lista)
print(f'{d:.2f}')
