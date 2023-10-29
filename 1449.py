a=int(input())
for n in range(a):
    dic={}
    b,c=map(int, input().split())
    for n in range(b):
        pala=input()
        vra=input()
        dic.update({pala:vra})
    dead=dic.keys()
    for n in range(c):
        lista=[]
        frase=list(map(str, input().split()))
        for n in range(len(frase)):
            if frase[n] in dead:
                lista.append(dic[frase[n]])
            else:
                lista.append(frase[n])
        print(' '.join(lista))
    print()
