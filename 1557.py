while True:
    try:
        a=int(input())
        if a==0:
            break
        else:
            lista=[]
            for n in range(a):
                linha=[]
                for h in range(a):
                    d=2**(h+n)
                    d=str(d)
                    linha.append(d)
                lista.append(linha)
            T = len(str(lista[a - 1][a - 1]))
            for i in range(a):
                for j in range(a):
                    lista[i][j] = str(lista[i][j])
                    while len(lista[i][j]) < T:
                        lista[i][j] = ' ' + lista[i][j]
                M = ' '.join(lista[i])

                print(M)
            print()

    except EOFError:
        break
