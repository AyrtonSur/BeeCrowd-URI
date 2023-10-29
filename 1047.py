inicio_h,inicio_m,fim_h,fim_m = map(int,input().split())

inicio = inicio_h*60 + inicio_m
fim = fim_h*60+ fim_m

if inicio < fim:
    tempo = fim - inicio
elif fim < inicio:
    tempo = ((24*60) - inicio) + fim
elif inicio == fim:
    tempo = (24*60)

hora = tempo / 60
minuto = tempo % 60

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"% (hora, minuto))
