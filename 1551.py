a=int(input())
for n in range(a):
    frase=str(input())
    l=0
    if 'a' in frase:
        l+=1
    if 'b' in frase:
        l+=1
    if 'c' in frase:
        l+=1
    if 'd' in frase:
        l+=1
    if 'e' in frase:
        l+=1
    if 'f' in frase:
        l+=1
    if 'g' in frase:
        l+=1
    if 'h' in frase:
        l+=1
    if 'i' in frase:
        l+=1
    if 'j' in frase:
        l+=1
    if 'k' in frase:
        l+=1
    if 'l' in frase:
        l+=1
    if 'm' in frase:
        l+=1
    if 'n' in frase:
        l+=1
    if 'o' in frase:
        l+=1
    if 'p' in frase:
        l+=1
    if 'q' in frase:
        l+=1
    if 'r' in frase:
        l+=1
    if 's' in frase:
        l+=1
    if 't' in frase:
        l+=1
    if 'u' in frase:
        l+=1
    if 'v' in frase:
        l+=1
    if 'w' in frase:
        l+=1
    if 'x' in frase:
        l+=1
    if 'y' in frase:
        l+=1
    if 'z' in frase:
        l+=1
    if l==26:
        print('frase completa')
    elif l<13:
        print('frase mal elaborada')
    elif l>13 and l<26:
        print('frase quase completa')
    
