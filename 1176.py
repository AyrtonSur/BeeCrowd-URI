e=int(input())
lista1=[0,1]
for h in range(0,61):
    b=lista1[h]+lista1[h+1]
    lista1.append(b)
for n in range(0,e):
    z=int(input())
    print(f'Fib({z}) = {lista1[z]}')
