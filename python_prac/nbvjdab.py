"""a="VenkatNarayanGrandhe"
b=[]
i=1
k=0
while(i<len(a)):
    if ord(a[i])<97:
        b.append(a[k:i])
        k=i
    i+=1
b.append(a[k:])
print(b)
"""
"""
a=["amannath","amanraju","amankumar"]
b=a[0]
c=""
for i in range(1,len(a)):
    for j in range(len(a[i])):
        if a[j]!=b[j]:
            break
        else:
            c+=a[j]
        b=c
print(b)
"""
"""
class node():
    def __init__(self,data=None):
        self.data = data
        self.next = None
class llist():
    def __init__(self):
        self.head=node()
    def insert(self,data):
        m=self.head
        while(m.next!=None):
            m=m.next
        m.next=node(data)
    def display(self):
        m=self.head
        while(m.next!=None):
            m = m.next
            print(m.data)

a=llist()
a.insert(9)
a.insert(2)
a.insert(4)
a.display()
"""
class node:
    def __init__(self,data=None):
        self.data=data
        self.right=None
        self.left=None
class tree:
    def __init__(self,data):
        self.root=node(data)
    def get(self):
        print(self.root.data)
a=tree(10)
a.get()