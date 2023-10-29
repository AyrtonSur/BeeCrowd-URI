dic={'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
dic1={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
R=list(input())
G=list(input())
B=list(input())
a=len(R)-1
b=len(G)-1
c=len(B)-1
def hexadecimal(tamanho,palavra,dicio):
    soma=0
    beta=tamanho
    for n in range(tamanho + 1):
        if palavra[n] in dicio:
            goat = dicio[palavra[n]]
            soma += goat * 16 ** beta
            beta -= 1
        else:
            goat = int(palavra[n])
            soma += goat * 16 ** beta
            beta -= 1
    return soma
soma=1
verm=hexadecimal(a,R,dic)
verd=hexadecimal(b,G,dic)
azul=hexadecimal(c,B,dic)
qVerm = 1
qVerd = (verm // verd) * (verm // verd)
qAzul = ((verd // azul) * (verd // azul)) * qVerd
tudo = qVerm + qVerd + qAzul
lista=[]
while tudo!=0:
    n=tudo%16
    tudo=tudo//16
    lista.append(n)
lista.reverse()
for n in range(len(lista)):
    if lista[n] in dic1:
        lista[n]=str(dic1[lista[n]])
    else:
        lista[n]=str(lista[n])
print(''.join(lista))
