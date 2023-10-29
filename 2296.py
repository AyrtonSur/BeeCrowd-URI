m = int(input())
tm = []
for i in range(m):
    sumid = 0
    sumvo = 0
    listatr = input().split()
    listatr = [int(n) for n in listatr]
    for z in range(1, listatr[0]):
        if listatr[z+1] >= listatr[z]:
            sumid += listatr[z+1] - listatr[z]
    for z in range(0, listatr[0] - 1):
        if listatr[listatr[0] - z] <= listatr[listatr[0] - z - 1]:
            sumvo += listatr[listatr[0] - z - 1] - listatr[listatr[0] - z]
    tm.append(min(sumid,sumvo))
melhor_caminho = sorted(tm)[0]
print(tm.index(melhor_caminho) + 1)
