v=0
while True:
    try:
        a=int(input())
        if a!=0:
            lista=[]
            A=[]
            B=[]
            C=[]
            D=[]
            E=[]
            l1=[]
            l2=[]
            l3=[]
            l4=[]
            l5=[]
            l6=[]
            v+=1
            for n in range(a):
                d=list(map(str, input().split()))
                A.append(d[0])
                A.append(d[1])
                B.append(d[2])
                B.append(d[3])
                C.append(d[4])
                C.append(d[5])
                D.append(d[6])
                D.append(d[7])
                E.append(d[8])
                E.append(d[9])
                for p in range(10,16):
                    if d[p]=='A':
                        x=A[0]
                        z=A[1]

                    elif d[p]=='B':
                        x=B[0]
                        z=B[1]
                    elif d[p]=='C':
                        x=C[0]
                        z=C[1]
                    elif d[p]=='D':
                        x=D[0]
                        z=D[1]
                    elif d[p]=='E':
                        x=E[0]
                        z=E[1]
                    if p==10:
                        l1.append(x)
                        l1.append(z)
                    elif p==11:
                        l2.append(x)
                        l2.append(z)
                    elif p==12:
                        l3.append(x)
                        l3.append(z)
                    elif p==13:
                        l4.append(x)
                        l4.append(z)
                    elif p==14:
                        l5.append(x)
                        l5.append(z)
                    elif p==15:
                        l6.append(x)
                        l6.append(z)
                A.clear()
                B.clear()
                C.clear()
                D.clear()
                E.clear()
            from collections import Counter
            count1=Counter(l1)
            count2=Counter(l2)
            count3=Counter(l3)
            count4=Counter(l4)
            count5=Counter(l5)
            count6=Counter(l6)
            lista1=count1.most_common(1)
            lista2=count2.most_common(1)
            lista3=count3.most_common(1)
            lista4=count4.most_common(1)
            lista5=count5.most_common(1)
            lista6=count6.most_common(1)
            print(f'Teste {v}')
            print(f'{lista1[0][0]} {lista2[0][0]} {lista3[0][0]} {lista4[0][0]} {lista5[0][0]} {lista6[0][0]} \n')
            l1.clear()
            l2.clear()
            l3.clear()
            l4.clear()
            l5.clear()
            l6.clear()
        else:
            break
    except EOFError:
        break

#the solution I used here is quite overwhelming (i think that's the word), but it's quite fun to make this code, feel free to use it (or not).
