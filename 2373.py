a=int(input())
d=0
for n in range(a):
    b,c=map(int, input().split())
    if b>c:
        d+=c
print(d)
