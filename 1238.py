a=int(input())
for n in range(a):
    b,c=map(str, input().split())
    d=''
    l=0
    for n in range(min(len(b),len(c))):
        d+=b[n]
        d+=c[n]
        l+=1
    if len(b)>len(c):
        for h in range(len(b)-l):
            d+=b[h+l]
    elif len(b)<len(c):
        for h in range(len(c)-l):
            d+=c[h+l]
    print(d)
