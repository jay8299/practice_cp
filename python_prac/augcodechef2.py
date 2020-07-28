def res(number,value):
    if number<value//2:
        return 1
    elif number%2==0:
        return res(number-1,value-1)
    else:
        return (value-1)*res(number-1,value-1)
print(res(7,4))