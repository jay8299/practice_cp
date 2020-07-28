a=input()
a=list(a)
a[0]=a[0].upper()
print(a[0])
for i in range(len(a)):
    if(a[i]==' '):
        a[i+1]=a[i+1].upper()
z=''.join(a)
print(z)