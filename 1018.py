n1=int(input())
n2=n1//100
k1=n1%100
n3=k1//50
k2=k1%50
n4=k2//20
k3=k2%20
n5=k3//10
k4=k3%10
n6=k4//5
k5=k4%5
n7=k5//2
k6=k5%2
n8=k6//1
print(n1)
print(f'{n2} nota(s) de R$ 100,00')
print(f'{n3} nota(s) de R$ 50,00')
print(f'{n4} nota(s) de R$ 20,00')
print(f'{n5} nota(s) de R$ 10,00')
print(f'{n6} nota(s) de R$ 5,00')
print(f'{n7} nota(s) de R$ 2,00')
print(f'{n8} nota(s) de R$ 1,00')
