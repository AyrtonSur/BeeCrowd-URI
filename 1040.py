a,b,c,d=map(float, input().split())
e=((a*2)+(b*3)+(c*4)+(d*1))/10
print(f'Media: {e:.1f}')
if e>=7:
    print('Aluno aprovado.')
elif e>=5 and e<7:
    print('Aluno em exame.')
    i=float(input())
    print(f'Nota do exame: {i:.1f}')
    h=(i+e)/2
    if h>=5:
        print('Aluno aprovado.')
        print(f'Media final: {h:.1f}')
    if h<5:
        print('Aluno reprovado')
        print(f'Media final: {h:.1f}')
elif e<5:
    print('Aluno reprovado.')
