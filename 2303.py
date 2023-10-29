a,b,c,d=map(int, input().split())
matriz=[]
for n in range(a):
    linha=list(map(int, input().split()))
    matriz.append(linha)
e=0
lista=[]
for j in range(0,a,c):
    for k in range(0,b,d):
        for n in range(0,c):
            for h in range(0,d):
                e+=matriz[n+j][k+h]
        lista.append(e)
        e=0
print(max(lista))
