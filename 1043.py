a,b,c=map(float, input().split())
if a>=b and a>=c:
    if a<c+b:
        e=a+b+c
        print(f'Perimetro = {e:.1f}')
    if a>=b+c:
        e=((a+b)*c/2)
        print(f'Area = {e:.1f}')
elif b>=c and b>=a:
    if b<a+c:
        e=a+b+c
        print(f'Perimetro = {e:.1f}')
    if b>=a+c:
        e=((a+b)*c/2)
        print(f'Area = {e:.1f}')
elif c>=a and c>=b:
    if c<a+b:
        e=a+b+c
        print(f'Perimetro = {e:.1f}')
    if c>=a+b:
        e=((a+b)*c/2)
        print(f'Area = {e:.1f}')
