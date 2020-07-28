N=int(input())
v=input().split(' ')
a=[]
for i in range(N):
    n=v[i]
    N=list(n)
    for i in range(len(N)):
        N[i]=int(N[i])
    lar=max(N)
    sma=min(N)
    bi=11*lar+7*sma
    if(bi>99):
        bi=bi/100
        vi=str(bi)
        vi=vi.split('.')
        bi=int(vi[1])
    a.append(bi)
b=a
gev=[]
god=[]
gev1=[]
god1=[]
cx=[]
cy=[]
for i in range(len(b)):
    if(i%2==0):
        gev.append(b[i])
    if(i%2!=0):
        god.append(b[i])

for i in range(len(gev)):
    gev1.append((gev[i]//10))
gev1.sort()
for i in range(len(gev1)):
    if(gev1.count(gev1[i])>1 and gev1[i+1]!=gev1[i]):
        cx.append(gev1.count(gev1[i]))

for i in range(len(god)):
    god1.append((god[i]//10))
god1.sort()
for i in range(len(god1)):
    if(god1.count(god1[i])>1 and god1[i+1]!=god1[i]):
        cy.append(god1.count(god1[i]))

z=sum(cx)-len(cx)+sum(cy)-len(cy)
print(z)