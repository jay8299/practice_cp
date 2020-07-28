try:
    import math
    n=int(input())
    while(n>0):
        a=list(map(int,input().split(' ')))
        N=a[0]
        K=a[1]
        if(N%(K**2)==0):
            print("NO")
        else:
            print("YES")

        n-=1
except:
    pass