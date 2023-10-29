t=0
j=0

while True:
    try:
        x1,y1,x2,y2=map(int, input().split())
        if x1!=0 and x2!=0 and y1!=0 and y2!=0:
            v = 0
            j += 1
            n = int(input())
            print(f'Teste {j}')
            for x in range(0,n):
                a,b=map(int, input().split())
                if a in range(x1,x2+1):
                    t+=1
                if b in range(y2,y1+1):
                    t+=1
                if t==2:
                    v+=1
                t=0
            print(v)
        else:
            break
    except EOFError:
        break
