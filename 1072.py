h=int(input())
g=0
o=0
for e in range(0,h):
    n=int(input())
    if n in range(10,20+1):
        g+=1
    else:
        o+=1
print(f'{g} in')
print(f'{o} out')
