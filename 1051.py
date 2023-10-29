n1=float(input())
if n1>=0 and n1 <= 2000:
    print('Isento')
if n1> 2000 and n1 <= 3000:
    n2=(n1-2000)*0.08
    print(f'R$ {n2:.2f}')
if n1> 3000 and n1 <= 4500:
    n2=1000*0.08+(n1-3000)*0.18
    print(f'R$ {n2:.2f}')
if n1> 4500:
    n2=1000*0.08+1500*0.18+(n1-4500)*0.28
    print(f'R$ {n2:.2f}')
