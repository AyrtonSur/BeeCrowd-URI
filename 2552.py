while True:
    try:
        a,b=map(int, input().split())
        matriz=[]
        for n in range(a):
            linha=list(map(int, input().split()))
            matriz.append(linha)
        gap=[]
        for n in range(a):
            op=[]
            for h in range(b):
                g=0
                if matriz[n][h]==0:
                    if n+1<a and matriz[n+1][h]==1:
                        g+=1
                    if h+1<b and matriz[n][h+1]==1:
                        g+=1
                    if n>0 and matriz[n-1][h]==1:
                        g+=1
                    if h>0 and matriz[n][h-1]==1:
                        g+=1
                    op.append(g)
                elif matriz[n][h]==1:
                    op.append(9)
            gap.append(op)
        for n in range(len(gap)):
            resu=''.join(map(str, gap[n]))
            print(resu)
    except EOFError:
        break
