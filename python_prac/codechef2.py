# cook your dish here
try:
    n=int(input())

    while(n>0):
        m=int(input())
        a=list(map(int,input().split(' ')))
        s=0
        f=0
        for i in range(m):
            for j in range(i):
                f=sum(list(map(int,list(str(a[i]*a[j])))))
                if(f>s):
                    s=f
        print(s)

        n-=1
except:
    pass