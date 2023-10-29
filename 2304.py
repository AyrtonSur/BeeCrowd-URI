a,b=map(int, input().split())
d=a
e=a
f=a
for n in range(b):
    lista1=list(map(str ,input().split()))
    if len(lista1)==3:
        if lista1[0]=='V':
            if lista1[1]=='D':
                d=int(lista1[2])+d
            elif lista1[1] == 'E':
                e=int(lista1[2])+e
            elif lista1[1] == 'F':
                f=int(lista1[2])+f
        elif lista1[0]=='C':
            if lista1[1]=='D':
                d=d-int(lista1[2])
            elif lista1[1] == 'E':
                e=e-int(lista1[2])
            elif lista1[1] == 'F':
                f=f-int(lista1[2])
    else:
        if lista1[1] == 'D':
            if lista1[2]=='E':
                d=int(lista1[3])+d
                e=e-int(lista1[3])
            elif lista1[2]=='F':
                d=int(lista1[3])+d
                f=f-int(lista1[3])
        elif lista1[1] == 'E':
            if lista1[2]=='D':
                e=int(lista1[3])+e
                d=d-int(lista1[3])
            elif lista1[2]=='F':
                e=int(lista1[3])+e
                f=f-int(lista1[3])
        elif lista1[1] == 'F':
            if lista1[2]=='D':
                f=int(lista1[3])+f
                d=d-int(lista1[3])
            elif lista1[2]=='E':
                f=int(lista1[3])+f
                e=e-int(lista1[3])

    lista1.clear()
print(d,e,f)
