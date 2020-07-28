# cook your dish here
def swap(a,x,y):
    i=a[x]
    a[x]=a[y]
    a[y]=i
    return a

n=int(input())
while(n>0):
    print("1")
    m=int(input())
    a=list(map(int,input().split(' ')))
    k=0
    d=[]
    o=0
    while(k<m-1):
        print("2")
        d=swap(a,k,k+1)
        print(d)
        h=1
        z=[]
        for i in range(len(d)):
            z.append(h*d[i])
            h+=1
        print(z)
        u=sum(z)
        if(u>o):
            o=u
        k+=1
    print(o)
    n-=1
