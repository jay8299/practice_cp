"""
#reverse the string
a="feb@ffh@t5g?hig*u$"
i=0
b=[]
c=[]
while(i<len(a)):
    if ord(a[i])>31 and ord(a[i])<49:
        b.append(a[i])
    else:
        c.append(a[i])
        b.append("dummy")
    i+=1
c=list(reversed(c))
print(b,c)
j=0
for i in range(len(a)):
    if b[i]=="dummy":
        b[i]=c[j]
        j+=1
    else:
        continue
print(b)
"""

"""
#
a=[6,4,3,5,4,3,2,8,1,6]

first=a.index(5)
last=a.index(8)
b=int("".join(list(map(str,a[first+1:last]))))
print(b+sum(a[:first])+sum(a[last+1:]))
"""
"""

a="{([]){"
a=list(a)
b=[]
for i in a:
    if i==']':
        l=a.index('[')
        m=a.index(']')
        if l!=m+1:
            print(m+1)
            break
        else:
            del a[l]
            del a[m]

    elif i==')':
        l=a.index('(')
        m=a.index(')')
        if l!=m+1:
            print(m+1)
            break
        else:
            del a[l]
            del a[m]
    elif i=='}':
        l=a.index('{')
        m=a.index('}')
        if l!=m+1:
            print(m+1)
            break
        else:
            del a[l]
            del a[m]
    else:
        b.append(i)
else:
    print(0)
"""

"""

#sum to last number

from itertools import combinations
a=sorted([2,3,6,11,1,2,4,7])
j=len(a)
flag=0
while(j>1):
    for i in combinations(a,j):
        #print(i)
        if sum(i[:-1])==i[-1]:
            print("ans",i)
            print(min(i))
            flag=1
            break
    if flag:
        break
    j-=1


"""


"""

#lagrgest even number

a="ab73bffn9135"
p=[]
for i in a:
    if i>='0' and i<='9':
        p.append(i)
p.sort(reverse=True)
i=len(p)-1
if int(p[-1])%2==0:
    print(int(''.join(p)))
else:
    while(i>=0):
        if int(p[i])%2==0:
            temp=p[i]
            del p[i]
            p.append(temp)
            print(int(''.join(p)))
            break
        i-=1
    else:
        print(-1)

"""

"""

from itertools import permutations,combinations
a=[1,1,2]
l=len(set(list(permutations(a,3))))
a=list(permutations(a,3))
a.sort()
s=str(a[-1][0])+str(a[-1][1])+str(a[-1][2])
print(s,l)

"""

"""

def pal(a):
    a=list(str(a))
    i=0
    j=len(a)-1
    while(i<j):
        if a[i]!=a[j]:
            return False
        i+=1
        j-=1
    return True
a = int(input())
while(1):
    g=list(reversed(list(str(a))))
    a+=int(''.join(g))
    #print(a)
    if pal(a):
        break
print(a)

"""


"""
a=["fngjkn",'59','20',"jehbrjk"]
p=[]
for i in a:
    if i[0]>='0' and i[0]<='9':
        if int(i)%2!=0:
            p.append(int(i))
print(p)
"""
"""
a=[1,21,34]
g=""
for i in a:
    g+=str(i)
print(int(g))
"""
"""
class A:
    def __init__(self,n,m):
        self.__n=n
        self.m=m
    def display(self):
        print(self.__n,self.m)
r=A(10,20)
r.display()
print(r._A__n)
"""

"""
#rearrange the order
a="1232245211"
e=[]
o=[]
for i in a:
    if int(i)%2:
        o.append(i)
    else:
        e.append(i)
i=0
j=0
g=""
while(i<len(e) and j<len(o)):
    g+=e[i]
    i+=1
    g+=o[j]
    j+=1
g+="".join(e[i:])
g+="".join(o[j:])
print(g)
"""



"""
a=[1,2,2,3,4]
num=2
i=0
b=[]
while(i<len(a)):
    if a[i]==num:
        if i-1>=0:
            b.append(i-1)
        if i+1<len(a):
            b.append(i+1)
        b.append(i)
    i+=1
b=list(set(b))
for i in range(len(b)):
    b[i]=a[b[i]]
for i in b:
    a.remove(i)
print(a,sum(a))
"""
"""

fc=10
oc=5
amt=66

if 5*fc>=amt:
    fc-=amt//5
    oc-=amt%5
    print(fc,oc)
else:
    x=amt//5
    y=amt%5
    oc-=y
    if fc<x:
        print("five rupee coins needed ",x-fc)
    else:
        print("five coins left ",fc)
    if oc<y:
        print("one rupee coins needed ",y-oc)
    else:
        print("one coins left ",oc)


"""
"""
a=[1,2,3,4,5,6,7]
o=0
e=0
for i in a:
    if i%2:
        o+=1
    else:
        e+=1
print(o,e)

"""

"""
a=[-1,2,3,-4,0,5,-7,4,-3]
pos=0
neg=0
for i in a:
    if i>=0:
        pos+=1
    else:
        neg+=1
print(pos,neg)
"""
"""
n=2
a=[1,7,3,5,6,8,1,3,0]
a.sort()
print(a[:n])
"""
"""
a=map(int,list("1232245211"))
p=[]
d={}
for i in a:
    d[i]=d.get(i,0)+1
for i,j in d.items():
    p.append([i]*j)
print(p)

"""
"""
#subsequence
a=input()
i=len(a)-1
f=0
p=[]
while(i>0):
    for j in range(i):
        if sorted(set(list(a[j:i+1]))) == sorted(list(a[j:i+1])):
            p.append(a[j:i+1])
    i-=1
print(sorted(p,key=len)[-1])
"""
"""

a="143"
b=3
x=int(a)%9
if x==0:
    print(9)
else:
    print(sum(map(int,list(str(x*b)))))

"""

"""
def fun(st1):
    f=['a','e','i','o','u']
    st=[]
    r=""
    for i in st1:
        if i not in f:
            st.append(i)
        if i=='#':
            st.pop()
        print(st)
    while st!=[]:
        r+=st.pop()

    print(r)
fun("hi##jack")
"""
"""
#regex assignment

import re
a="lathah067@gmail.com"
print(re.sub("\s","**",a))
print(re.sub("","**",a))
print(re.sub("\S","**",a))
print(re.sub("\D","**",a))
print(re.sub("\W","**",a))
print(re.sub("\w","**",a))
print(re.sub("\B","**",a))
print(re.search("[a-z[0-9]{4}.]+\@[a-g]\.[c-o]",a))
"""

"""
class A:
    x=50
    def __init__(self):
        self.__num=10
        self.__y=100
    def __prtt(self):
        self.num1=0
        print(self.num1)
    def mot(self):
        __prtt()
a=A()
a.mot

#a.x=100

"""
"""
class polygon:
    def __init__(self):
        self.data=100
        self.__b=500
    def getter(self):
        print(self.__b)
class triangle(polygon):
    def prt(self):
        #super().__init__()
        print(self.data)
        self.getter()
a=triangle()
a.prt()

"""


"""
import re

a=['AZ01-1234','R137-8714','HR05-2941']
#a=['GT21-1011','S621-9699']
b=[]
for i in a:
    g,h=i.split("-")
    y=re.split("[^A-Z]",g)
    l=len(max(y))
    if l==1:
        h=h[1:]+h[0]
        b.append(max(y)+h)
    elif l==2:
        h=h[2:]+h[:2]
        b.append(max(y)+h)
print(b)
"""



"""
a="((2))(((3)))"
l=[]
i=0
while i<len(a):
    if l==[] and (a[i]=="}" or a[i]=="]" or a[i]==")"):
        print(False)
        break
    elif a[i]=="{" or a[i]=="[" or a[i]=="(":
        l.append(a[i])
    elif ord(a[i])>47 and ord(a[i])<59:
        c=int(a[i])
        x=c
        while(c>0 and l!=[]):
            l.pop()
            c-=1
        if l!=[] or c!=0:
            print(False)
            break
        else:
            i+=x+1
            continue
    i+=1
else:
    print(True)

"""
"""
#2nd and #3rd
prices = {'ACME': 45.23,'AAPL': 612.78, 'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}
x={k:v for k,v in prices.items() if v>200}
print(x)
"""
"""
#4th
a=[1, 2, 9, 3, 4]
print(9 in a[:5])
"""
"""
#5th
a=[1, 1,2,4,3]
p=[-1,-1,-1]
x=[1,2,3]
for i in range(len(x)):
    for j in range(len(a)):
        if x[i]==a[j]:
            p[i]=j
print(p[0]==p[1]-1 and p[1]==p[2]-1)
"""
"""
#6th
a,b=123,738
p=1
for i in map(int,list(str(a))):
    p*=i
print(a*p==b)
"""
"""
#8th
n=int(input())
print({ i:i**2 for i in range(1,n+1)})
"""
"""
#9th
a="w3resource"
if len(a)==2:
    print(a*2)
elif len(a)<2:
    print(-1)
else:
    print(a[:2]+a[-2:])
"""
"""
#10th and 11th
a="Welcome to Mysore"
u=0
l=0
for i in a:
    if ord(i)>64 and ord(i)<92:
        u+=1
    elif ord(i)>96 and ord(i)<123:
        l+=1
print([u,l])
"""
"""
#13th
subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            print(subjects[i]+" "+verbs[j]+" "+objects[k])
"""
"""
#14th
a=[ 3,2,5,1,2,1,2]
try:
    i=0
    p=[]
    while(1):
        i=a.index(2,i+1)
        p.append(i)
except:
    for i in range(1,len(p)):
        if p[i]==p[i-1]+1:
            print(True)
            break
    else:
        print(False)
"""
"""
#15th
n=int(input())
for i in range(n):
    print("."*i+"*")
"""

"""
#16th
a=int(input())
print(a%int(sum(map(int,list(str(a)))))==0)
"""
"""
#17th and 19th
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,b%a)
a,b=800,2800
print(gcd(a,b))
"""
"""
#18th
a=['cat', 'Come']
print([ len(i) for i in a])
"""
"""
from abc import ABC,abstractclassmethod
class poly(ABC):
    def prt():
        print("in poly")
class tri(poly):
    def prt(self):
        print("in tri")
a=poly
print(a.prt())
b=tri()
print(b.prt())
"""
"""
a="1203456"
b=list(a)
p=[]
for i in range(1,len(b)):
    if b[i]>b[i-1]:
        if str(int(b[i])*int(b[i-1])) in a:
            p.append(str(int(b[i])*int(b[i-1])))
print(p)
"""
"""
import re
a="3$5&^*7264&"
b=re.split("[0-9]",a)
x=re.split("[^0-9]",a)
d,c=[],[]
for i in x:
    c.extend(list(i))
for i in b:
    d.extend(list(i))
o,e=[],[]
for i in c:
    if int(i)%2:
        o.append(i)
    else:
        e.append(i)
g=""
if len(d)%2:
    i=0
    j=0
    while(i<len(o) and j<len(e)):
        g+=o[i]
        g+=e[j]
        i+=1
        j+=1
    g+="".join(o[i:])
    g+="".join(e[i:])
else:
    i = 0
    j = 0
    while (i < len(e) and j < len(o)):
        g += e[i]
        g += o[j]
        i += 1
        j += 1
    g += "".join(e[i:])
    g += "".join(o[i:])
print(g)
"""
"""
a="12630"
i=1
j=2
while(i*j<int(a)):
    if str(i*j) in a:
        print(f"{i*j}({i}*{j})")
    i+=1
    j+=1
"""
"""
#20
a="Jet on the Mat but mat is too long"
p="jet"
q="mat"
print(a.upper().count(q.upper())==a.upper().count(p.upper()))
"""
"""
#21st
a=[1,2,3,4,5,6,7,8,9,10]
p=[]
p.extend(a[len(a):len(a)//2-1:-1])
p.extend(a[:len(a)//2])
print(p)
"""
"""
#22nd
list,number=[1,2,2,3,5,4,2,2,1,2],2
m=[]
for i in range(len(list)):
    if list[i]==number:
        m.append(i)
        if i+1<len(list):
            m.append(i+1)
        if i-1>=0:
            m.append(i-1)
print(m)
m=set(m)
q=[]
for i in m:
    q.append(list[i])
for i in q:
    list.remove(i)
print(list)
"""
"""
#23rd
a,b=map(int,input().split(","))
print(10 in [a,b] or a+b==10)
"""
"""
#24th and 25th
a,b=map(int,input().split(","))
x=[]
for i in range(a):
    y=[]
    for j in range(b):
        y.append(str(i)+","+str(j))
    x.append(y)
print(x,x[0][0])
"""
#assignment2
"""
#2nd
l,p=[1, 2, 3, 4, 5, 6],4
k=list(l[:len(l)-p])
v=l[-p:]
v.extend(k)
print(v)
"""
"""
#3rd
a=[1, 2, 3, 4, 5, 6]
x=[]
for i in range(len(a)):
    y=[a[i]]
    for j in range(i+1,len(a)):
        if a[j]%a[i]==0:
            y.append(a[j])
    if y!=[a[i]]:
        x.append(y)
print(x)
"""
"""
#4th
def fun(n):
    p=[]
    for i in range(n):
        for j in range(i,n):
            if i**2+j**2==n:
                p.append([i,j])
    return p!=[]
print(fun(25))
"""
"""
#5th
n=int(input())
if not n>0 and n<1001:
    print(-1)
else:
    a=["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","ninteen"]
    c=["twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
    d=["hundred","thousand"]
    if n<20:
        print(a[n-1])
    else:
        if len(str(n))==2:
            g=c[int(str(n)[0])-2]+" "+a[int(str(n)[1])-1]
            print(g)
        elif len(str(n))==3:
            g=a[int(str(n)[0])-1]+" "+d[0]+" "+"and"+" "
            if int(str(n)[1])>=2:
                g+=c[int(str(n)[1]) - 2]+" "+a[int(str(n)[2]) - 1]
            elif int(str(n)[1])==1:
                g+= a[int(str(n)[1:])- 1]
            else:
                g+= a[int(str(n)[2]) - 1]
            print(g)
        elif n==1000:
            print(a[0]+" "+d[1])
"""

"""
#6th
def fun(a,b):
    if type(a)==list and len(a)>=2 and a[0] in list(b) and list not in [type(i) for i in a]:
        #print("in base")
        return True
    else:
        if len(a)<2:
            return False
        for i in a:
            if type(i)!=list and type(i)!=str:
                #print("not str or list")
                return False
            elif type(i)==list:
                #print(i,"in recur")
                return fun(i,b)
print(fun(['VP', ['VP', 'eat']],['VP']))
"""
"""
a="1456734512345698"
k=list(map(int,a))
b=list(a[len(a)-2::-2])
d=list(a[len(a)-1::-2])
d=map(int,d)
for i in range(len(b)):
    b[i]=int(b[i])*2
    if b[i]>9:
        b[i]=sum(map(int,str(b[i])))
if (sum(d)+sum(b))%10:
    print("Not Valid")
else:
    print("Valid")
"""
"""
from itertools import permutations
soe=[True]*(10001)
for i in range(2,10000):
    if soe[i]:
        for j in range(i+i,10000,i):
            soe[j]=False
def prime(n):
    global soe
    return soe[n]
n=int(input())
g=[]
for j in range(2,n+1):
    d=0
    c=len(list(permutations(list(str(j)),len(list(str(j))))))
    for i in permutations(list(str(j)),len(list(str(j)))):
        prt=''.join(list(i))
        if prime(int(prt)):
            d+=1
    if c==d:
        g.append(j)
print(g)
"""
"""
t = int(input())
for p in range(1, t + 1):
    n, m = map(int, input().split(" "))
    a = list(map(int, input().split(" ")))
    a.sort()
    s = 0
    c = 0
    for i in a:
        s += i
        if s > m:
            print(f"Case #{p}: {c}")
            break
        elif s == m:
            c += 1
            print(f"Case #{p}: {c}")
            break
        else:
            c += 1
"""
"""
t = int(input())
for i in range(1, t + 1):
    n, k, p = [int(g) for g in input().split(" ")]
    a = []
    j = 0
    while j < n:
        p = [int(g) for g in input().split(" ")]
        a.append(p)
        j += 1
    for ik in range(n):
"""
"""

def sum_of_stacks(stacks):
    maximum_values = []

    for stack in stacks:
        maximum_values.append(find_max(stack))

    return sum(maximum_values)


def find_max(stack):
    is_maximum_value = 0

    for i in stack:
        if i > is_maximum_value:
            is_maximum_value = i

    return is_maximum_value


t=int(input())
for i in range(t):
    n,k,p=
    sum_of_stacks([[1, 8, 100, 3], [2000, 2, 3, 1], [10, 1, 4]])
"""
"""

def findMinLength(strList):
    return len(min(it, key=len))


def allContainsPrefix(strList, str,
                      start, end):
    for i in range(0, len(strList)):
        word = strList[i]
        for j in range(start, end + 1):
            if word[j] != str[j]:
                return False
    return True

def CommonPrefix(strList):
    index = findMinLength(strList)
    prefix = ""
    low, high = 0, index - 1
    while low <= high:

        # Same as (low + high)/2, but avoids
        # overflow for large low and high
        mid = int(low + (high - low) / 2)
        if allContainsPrefix(strList,
                             strList[0], low, mid):

            # If all the strings in the input array
            # contains this prefix then append this
            # substring to our answer
            prefix = prefix + strList[0][low:mid + 1]

            # And then go for the right part
            low = mid + 1
        else:

            # Go for the left part
            high = mid - 1

    return prefix
from itertools import combinations
t=int(input())
for i in range(t):
    n,k=list(map(int,input().split()))
    a=[]
    for j in range(n):
        a.append(input())
    s=[0]
    for it in combinations(a,k):
        #print(it)
        p=CommonPrefix(it)
        if len(p)>s[-1]:
            s.append(len(p))
    print(sum(s))

"""


#find cities
l=list(input().split(","))
for i in range(len(l)):
    l[i]=list(l[i].split(":"))
print(l)
arr1=sorted(l,key=lambda x:int(x[1]))
arr2=sorted(l,key=lambda x:int(x[2]),reverse=True)
outstr=""
print(arr1)
print(arr2)
for i in range(len(l)):
    if arr1[i][0]==arr2[i][0]:
        outstr+=arr1[i][0]+":"
if outstr=="":
    print("X")
else:
    print(outstr[:-1])

        










































