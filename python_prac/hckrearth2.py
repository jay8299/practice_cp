def nm(a):
    b=1
    f=[]
    while(b<=len(a)):
        f.append(sum(a[0:b]))
        b+=1
    return f
n=list(map(int,input().split(' ')))
y=list(map(int,input().split(' ')))
o=1
d=y
while(o<=n[1]):
    h=n[2]
    p=[]
    for i in range(n[0]):
        p.append(y[i]**o)
    x=p
    while(h>0):
        f=nm(x)
        x=f
        h-=1
    print(f[2],end=' ')
    o+=1


