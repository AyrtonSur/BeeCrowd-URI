a=int(input())
matriz=[]
for n in range(a):
    linha=list(input())
    fec=len(linha)
    for h in range(len(linha)):
        if linha[h].isalpha():
            poc=ord(linha[h])
            poc+=3
            linha[h]=chr(poc)
        if h<=(fec-1)/2:
            doc=ord(linha[h])
            doc-=1
            linha[h]=chr(doc)
    linha.reverse()
    matriz.append(linha)
for n in range(len(matriz)):
    print(''.join(matriz[n]))
