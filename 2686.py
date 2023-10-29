while True:
    try:
        n = float(input())
    except EOFError:
        break

    if 0 <= n < 90 or n == 360:
        print('Bom Dia!!')
    elif 90 <= n < 180:
        print('Boa Tarde!!')
    elif 180 <= n < 270:
        print('Boa Noite!!')
    elif 270 <= n < 360:
        print('De Madrugada!!')

    tempo = 240 * ((n + 90) % 360)
    hora = ((tempo // 3600) % 24)
    minutos = ((tempo // 60) % 60)
    segundos = (tempo - (hora * 3600) - (minutos * 60))

    print(f'{hora:0>2.0f}:{minutos:0>2.0f}:{segundos:0>2.0f}')
