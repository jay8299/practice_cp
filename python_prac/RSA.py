def gcd(x,y):
    while(y):
        x,y=y,x%y
    return x
def fun(n):
    for i in range(2,n,1):
        if(gcd(i,n)==1):
            return i
p=int(input("enter prime number for 'p'"))
q=int(input("entre prime number for 'q'"))
M=int(input("enter message"))
print ("1:encrypt \n 2: decrypt")
s=int(input("enter"))
n=p*q
x=(p-1)*(q-1)
e=fun(x)
print ("Public Key is :")
print ("{"+str(e)+","+str(n)+"}")
m=x
a=e
c=0
for i in range(1,m+1):
    if((a*i)%m==1):
        d=i
        break;
print ("Private Key  is  :")
print ("{"+str(d)+","+str(n)+"}")
import math
if s==1:
    c=((math.pow(M,e))%n)
    print ("cipher text is : ")
    print (c)
else:
    p=((math.pow(M,d))%n)
    print ("plain text is : ")
    print (p)
