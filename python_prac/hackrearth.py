from itertools import combinations

n=list(map(int,input().split(' ')))
a=list(map(int,input().split(' ')))
b=[]
g=1
for i in range(n[0]):
    g*=(a[i]+1)

for i in range(n[0]):
    b.append(list(range(a[i]+1)))
i=0
j=0
d=[]
for i in range(n[0]):
    for j in range(a[i]+1):
        d.append(b[i][j])
#print(d)

z=list(set(combinations(d, n[0])))

x=len(z)
while(x>g):
    for i in range(n[0]):
        j=0
        while(j<x):
            if(z[j][i]>a[i]):
                del z[j]
            j+=1
            x=len(z)

k=[]
for i in range(len(z)):
    x=0
    for j in range(n[0]):
        x^=z[i][j]
    k.append(x)
for i in range(n[1]+1):
    print(k.count(i),end=' ')