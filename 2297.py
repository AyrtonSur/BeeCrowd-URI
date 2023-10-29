a=True
l=0
while a!=0:
    a=int(input())
    l+=1
    somaA=0
    somaB=0
    if a!=0:
        for n in range(a):
            aldo,beto=map(int, input().split())
            somaA+=aldo
            somaB+=beto
        print(f'Teste {l}')
        if somaA>somaB:
            print('Aldo')
        else:
            print('Beto')
        print()
