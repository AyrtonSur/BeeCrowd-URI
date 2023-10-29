a=list(map(int, input()))
if sum(a)%2==0:
    a.append(0)
elif sum(a)%2==1:
    a.append(1)
for n in range(len(a)):
    a[n]=str(a[n])
print(''.join(a))
