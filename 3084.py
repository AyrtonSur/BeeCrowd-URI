while True:
    try:
        a,b=map(int, input().split())
    except EOFError:
        break
    e=a/(360/12)%12
    f=b/(360/60)%60
    print(f'{e:0>2.0f}:{f:0>2.0f}')
