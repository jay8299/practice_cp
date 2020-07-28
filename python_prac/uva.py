n=int(input())
while(n>0):
    m=int(input())
    a=[]
    for i in range(m):
        a.append(int(input()))
    s=a[0]
    for i in range(m):
        j=i+1
        if(j<m-1 and a[j]>s):
            s=a[j]
    print(s-a[m-1],end='\n')
    n-=1
