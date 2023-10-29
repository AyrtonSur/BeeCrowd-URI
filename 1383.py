a=int(input())
l=0
for n in range(a):
    matriz=[]
    l+=1
    d=0
    for n in range(9):
        b=list(map(int, input().split()))
        matriz.append(b)
    for n in range(9):
        kobe=set(matriz[n])
        if len(kobe)!=9:
            d=1
            break
    if d!=1:
        matriz2=[]
        for n in range(9):
            linha=[]
            for h in range(9):
                linha.append(matriz[h][n])
            matriz2.append(linha)
        for n in range(9):
            kol=set(matriz2[n])
            if len(kol)!=9:
                d=1
                break
    if d!=1:
        matriz3=[]
        for n in range(3):
            for h in range(3):
                linha1=[]
                for k in range(3):
                    for g in range(3):
                        e=matriz[3*n+k][3*h+g]
                        linha1.append(e)
                matriz3.append(linha1)
        for n in range(9):
            kek=set(matriz3[n])
            if len(kek)!=9:
                d=1
                break
    if d==1:
        print(f'Instancia {l}')
        print('NAO')
        print()
    else:
        print(f'Instancia {l}')
        print('SIM')
        print()
