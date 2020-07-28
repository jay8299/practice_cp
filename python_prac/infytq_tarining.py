def sigma(x):
    w=[]
    i=1
    while(i*i<=int(x)):
        if int(x)%i==0:
            w.append(i)
            w.append(n//i)
        i+=1
    return sum(w)
n=int(input())
print(sigma(n)/n)