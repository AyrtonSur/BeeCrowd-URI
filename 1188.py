com=str(input())
lista=[]
for n in range(12):
    linha=[]
    for h in range(12):
        a=eval(input())
        linha.append(a)
    lista.append(linha)
f=lista[7][5]+lista[7][6]+lista[8][4]+lista[8][5]+lista[8][6]+lista[8][7]+lista[9][3]+lista[9][4]+lista[9][5]+lista[9][6]+lista[9][7]+lista[9][8]
c=lista[10][2]+lista[10][3]+lista[10][4]+lista[10][5]+lista[10][6]+lista[10][7]+lista[10][8]+lista[10][9]
e=lista[11][1]+lista[11][2]+lista[11][3]+lista[11][4]+lista[11][5]+lista[11][6]+lista[11][7]+lista[11][8]+lista[11][9]+lista[11][10]
d=e+c+f
if com=='S':
    print(f'{d:.1f}')
elif com=='M':
    b=d/144
    print(f'{b:.1f}')
