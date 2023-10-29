a=int(input())
f=0
for n in range(a):
    f+=1
    b,c=map(int, input().split())
    matriz=[]
    for n in range(b):
        linha=list(map(str, input().split()))
        matriz.append(linha)
    matriz.sort(key=lambda x: (-int(x[1]), int(x[2]), float(x[3]), len(x[0])))
    print('CENARIO {' + str(f) + '}')
    for n in range(c):
        print(f'{n+1} - {matriz[n][0]}')
    
