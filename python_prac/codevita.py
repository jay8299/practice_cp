
import math

#
# Complete the restaurant function below.
#
def restaurant(l,b):
    if(l==b):
        return 1
    else:
        x=list(map(int, str(math.sqrt(l)).split('.')))
        y=list(map(int ,str(math.sqrt(b)).split('.')))
        if(x[1]==0 or y[1]==0):
            return(min(l,b))
        else:
            return(l*b)

if __name__ == '__main__':
    n=int(input())
    g=[]
    for i in range(1,n+1):
        g.append(list(map(int,input().split(' '))))
    for i in g:
        #print(i[0],i[1])
        b=restaurant(i[0],i[1])
        print(b,end='\n')


