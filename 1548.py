a=int(input())
for n in range(a):
    l=0
    b=int(input())
    elem=list(map(int, input().split()))
    elem1=sorted(elem, reverse=True)
    for n in range(b):
        if elem[n]==elem1[n]:
            l+=1
    print(l)
