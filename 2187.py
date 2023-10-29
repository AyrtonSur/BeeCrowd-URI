n1=int(input())
i=0
while n1!=0:
    v1=n1//50
    n2=n1%50
    v2=n2//10
    n3=n2%10
    v3=n3//5
    n4=n3%5
    v4=n4//1
    i+=1
    print(f'Teste {i}')
    print(v1,v2,v3,v4)
    print('')
    n1=int(input())
