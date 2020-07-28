try:
    t=int(input())
    while(t>0):
        n=int(input())
        a=list(map(int, input().split(' ')))
        i=1
        j=2
        k=j
        u=0
        while(i<n and j<=k+1 and k<=n):
            print([i,j,k])
            #print('fcghvjbkn')
            f=0
            y=0
            for s in range(i-1,j):
                #print('cxvbn')
                #print(s)
                f^=a[s]
            for p in range(j,k):
                #print('sdfghjk')
                y^=a[p]
            print(y)
            print(f)
            if(y==f):
                u+=1
            if(k==n and j!=k):
                #print('pl,mnbv')
                j+=1
                k=j
            elif(j==k and k==n):
                #print('zxcvbn')
                i+=1
                j=i+1
                k=j
            else:
                k+=1
        print(u)
        t-=1
except:
    pass

