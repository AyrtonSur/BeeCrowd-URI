a=int(input())
for n in range(a):
    dic={}
    soma=0
    b=int(input())
    for n in range(b):
        chill,chile=map(str, input().split()) 
        dic.update({chill:float(chile)})
    c=int(input())
    for n in range(c):
        fruta,quant=map(str, input().split())
        soma+=dic[fruta]*int(quant)
    print(f'R$ {soma:.2f}')
