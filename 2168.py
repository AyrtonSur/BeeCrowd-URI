b=int(input())
lista=[]
results=[]
segurança=[]
port=''
for n in range(b+1):
    a=list(map(int, input().split()))
    lista.append(a)
for h in range(b):
    for n in range(b):
        d=lista[h][n]+lista[h][n+1]+lista[h+1][n]+lista[h+1][n+1]
        if d>=2:
            seguro='S'
            results.append(seguro)
        elif d<2:
            seguro='U'
            results.append(seguro)
for f in range(b):
    for d in range(b):
        port+=results[(f*b)+d]
    print(port)
    port=''
