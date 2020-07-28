''' ways to decode
m=1000000007
a=list(input().strip())
c=[0 for i in range(len(a)+1)]
c[0]=1
c[1]=1
for i in range(2,len(a)+1):
    c[i]=c[i-1]%m
    if (int(a[i-2])<=2 and int(a[i-1])<6):
        c[i]=(c[i]+c[i-2])%m
#print(c)
print(c[len(a)])
'''

'''
#Lics
a=list(map(int,input().split(" ")))
b=list(map(int,input().split()))
temp=[[0 for i in range(len(a)+1)] for j in range(len(b)+1)]
m=0
for i in range(len(a)+1):
    for j in range(len(b)+1):
        if(i!=0 and j!=0 and  a[i-1]==b[j-1]):
            temp[i][j]=temp[i-1][j-1]+1
            m=max(m,temp[i][j])
print(m)
'''

'''
#maxsumsubarray
a=list(map(int,input().split()))
k=0
m=0
for i in a:
    k+=i
    if k>m:
        m=k
    if k<0:
        k=0
print(m)
'''
'''
#max value parenthesis with + and - 
a="1+2-3+7"
op=['+','-']
def ev(arr,i,j):
    if len(arr)==1:
        return arr[0]
    if arr[j] =="+":
        #print("in plus")
        t=arr[i]
        arr=arr[j+1:]
        arr[0]=int(arr[0])+int(t)
    elif arr[j]=="-":
        #print("in minus")
        t=arr[i]
        arr=arr[j+1:]
        arr[0]=int(t)-int(arr[0])
    i=0
    j=i+1
    #print(arr)
    return ev(arr,i,j)
print(ev(list(a),0,1))    
'''
#leapleapfrog
"""
import bisect
a=list(map(int,input().split()))
b=[a[-1]]
for i in range(len(a)-2,-1,-1):
    if b[-1]<a[i]:
        b.append(a[i])
    else:
        p=bisect.bisect_left(b,a[i])
        b[p]=a[i]
print(b)
"""
"""
from itertools import combinations
a=[-2,-3,4.-1,-2,1,5,-3]*1
m=0
for i in range(1,len(a)):
    for j in combinations(a,i):
        m=max(m,sum(j))
print(m)
"""


"""
#Evaluate expression
print(eval("1+2-3+4"))
"""
"""
#sieve of erethosthanes
soearr=[True]*1000001
soearr[0]=soearr[1]=False
def soe():
    n=1000000
    global soearr
    for i in range(2, n+1):
        if soearr[i]:
            for j in range(i*i, n+1, i):
                soearr[j]=False
    for i in range(20):
        if soearr[i]:print(i)
soe()
def isthisprime(n):
    return soearr[n]
print(isthisprime(10))
"""
"""
soearr=[True]*1000001
soearr[0]=soearr[1]=False
def soe():
    n=1000000
    global soearr
    for i in range(2, n+1):
        if soearr[i]:
            for j in range(i*i, n+1, i):
                soearr[j]=False
    #for i in range(20):
    #    if soearr[i]:print(i)
soe()
def isthisprime(n):
    return soearr[n]
t=int(input())
while t>0:
    if isthisprime(int(input())):
        print("YES")
    else:
        print("NO")
    t-=1
"""
t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    a=list(map(int,input().split()))
    d=dict()
    d[a[0]]=0
    for i in range(1,n):
        d[a[i]]=d.get(a[i],i)
        if d[a[i]]!=i and d[a[i]]!=i-1:
            print("NO")
            break
        else:
            d[a[i]]=i
    else:
        print("YES")
