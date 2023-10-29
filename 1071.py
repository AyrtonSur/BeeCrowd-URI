n=int(input())
i=int(input())
e=0
if i >= n and n>=0:
    for g in range(n,i):
        if g%2==1:
            e += g
if n > i and i>=0:
    for g in range(i,n):
        if g%2==1:
            e += g
if i >= n and n<0:
    for g in range(n+1,i):
        if g%2==1:
            e += g
if n > i and i<0:
    for g in range(i+1,n):
        if g%2==1:
            e += g
print(e)
