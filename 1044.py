a,b=map(int, input().split())
if b>a:
    if b%a==0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
elif a>b:
    if a%b==0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
