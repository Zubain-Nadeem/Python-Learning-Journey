def gratest(a , b , c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c


a = 23 
b = 45
c = 35

print(f'The Greatest Number is {gratest(a , b , c)}')