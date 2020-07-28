soearr=[True]*100001
soearr[0]=soearr[1]=False
def soe():
    n=100000
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
from itertools import combinations
n,m=map(int,input().split(" "))
primelist=[]
for i in range(n,m+1):
    if soearr[i]:
        primelist.append(i)
l=[]
for i in range(len(primelist)):
    for j in range(len(primelist)):
        if primelist[j]!=primelist[i]:
            x=int(str(primelist[i])+str(primelist[j]))
            if isthisprime(x) and x not in l:
                l.append(x)
minimum=min(l)
maximum=max(l)
count=len(l)
arr=[minimum,maximum]
for i in range(2,count):
    arr.append(arr[-1]+arr[-2])
print(arr[-1])