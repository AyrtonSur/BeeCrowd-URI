n1=int(input())
x=0
lista2=[]
for n in range(0,n1):
    n2=int(input())
    for g in range(0,n2):
        instru=str(input()).upper()
        if instru=='LEFT':
            x-=1
            lista2.append('LEFT')
        elif instru=='RIGHT':
            x+=1
            lista2.append('RIGHT')
        else:
            a,b,c=map(str, instru.split())
            if lista2[int(c)-1]=='LEFT':
                x-=1
                lista2.append('LEFT')
            elif lista2[int(c)-1]=='RIGHT':
                x+=1
                lista2.append('RIGHT')
    lista2.clear()
    
            
    print(x)
    x=0
