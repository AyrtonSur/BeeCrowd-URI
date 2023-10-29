a=int(input())
for n in range(a):
    palavras=list(map(str, input().split()))
    lista = []
    for h in range(len(palavras)):
        if palavras[h]!='':
            lista.append(palavras[h][0])
    print(''.join(lista))
