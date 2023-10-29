a=list(map(int, input().split()))
b=sorted(a)
c=sorted(a, reverse=True)
l=0
d=0
for n in range(0,5):
    if a[n]==b[n]:
        l+=1
    if a[n]==c[n]:
        d+=1
if l==5:
    print('C')
elif d==5:
    print('D')
else:
    print('N')
