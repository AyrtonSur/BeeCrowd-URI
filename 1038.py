a,b=map(float, input().split())
if a==1:
    d=4
elif a==2:
    d=4.5
elif a==3:
    d=5
elif a==4:
    d=2
elif a==5:
    d=1.5
c=d*b
print(f'Total: R$ {c:.2f}')
