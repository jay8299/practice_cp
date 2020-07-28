import math
t=int(input())
a=dict()
c=0
while t>0:
    t-=1
    x,y,z=map(int,input().split())
    d=math.sqrt(x**2+y**2)
    time=d/z
    if time not in a:
        a[time]=a.get(time,1)
    else:
        a[time]+=1
print(a)
for i in a.values():
    c+=(i*(i-1)//2)
print(c)