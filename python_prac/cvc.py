n=int(input())
while(n>0):
    n-=1
    while(1):
        c=input()
        d=0
        for i in c:
            if(c.count(i)>1):
                d+=1
        if(d>1):
            print("Invalid")
            break
        c=list(c)
        if(len(c)>10):
            print("Invalid")
            break
        numbers = sum(i.isdigit() for i in c)
        words   = sum(i.isalnum() for i in c)
        caps  = sum(i.isupper() for i in c)
        if(numbers<3):
            print("Invalid")
            break
        if(caps<2):
            print("Invalid")
            break
        if(words<len(c)):
            print("Invalid")
            break

        print("Valid")
        break