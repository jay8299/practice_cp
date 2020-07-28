import itertools
#taking input
k=int(input())
a=list(map(int,input().split()))
#generating prime numbers
soe=[True]*(100000)
for i in range(2,100000):
    if soe[i]==True:
        j=i+i
        while j<100000:
            soe[j]=False
            j+=i
#storing prime numbers whith in given input
p=[i for i in range(2,len(soe)) if soe[i]==True and i<=a[0]]
c=0
g=0
for j in range(1,len(p)+1):
    for i in itertools.combinations(p,j):
        if soe[sum(i)]:
            #print(sum(i))
            c+=1
        if max(i)<=a[1]:
            g+=1
print(c%(10**16),g)







