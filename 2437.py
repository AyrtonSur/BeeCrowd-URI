xm,ym,xr,yr=map(int, input().split())
xd=xm-xr
yd=ym-yr
if xd<0:
    xd=xd*(-1)
if yd<0:
    yd=yd*(-1)
d=xd+yd
print(d)
