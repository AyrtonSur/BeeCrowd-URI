x0,y0,x1,y1=map(int, input().split())
v0,u0,v1,u1=map(int, input().split())
soma=0
if x0<=v0:
      if x1<v0:
            soma+=0
      else:
            soma+=1
elif v0<x0:
      if v1<x0:
            soma+=0
      else:
            soma+=1
if y0<=u0:
      if y1<u0:
            soma+=0
      else:
            soma+=1
elif u0<y0:
      if u1<y0:
            soma+=0
      else:
            soma+=1
if soma==2:
      print(1)
else:
      print(0)
