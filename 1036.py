a,b,c=map(float, input().split())
e=b**2-4*a*c
if a==0 or e<0 :
    print('Impossivel calcular')
else:
    r1=(-b+e**(1/2))/(2*a)
    r2=(-b-e**(1/2))/(2*a)
    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')
