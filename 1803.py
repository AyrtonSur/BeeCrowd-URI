matriz=[]
letra=''
for n in range(4):
    linha=list(input())
    matriz.append(linha)
a=len(linha)
matriz1=[]
for n in range(a):
    linha1=[]
    for h in range(4):
        b=matriz[h][n]
        linha1.append(b)
    matriz1.append(linha1)
lista=[]
for n in range(len(matriz1)):
    d=''.join(matriz1[n])
    lista.append(d)
for n in range(1,len(lista)-1):
    nem=(int(lista[0])*int(lista[n])+int(lista[-1]))%257
    letra+=chr(nem)
print(letra)
