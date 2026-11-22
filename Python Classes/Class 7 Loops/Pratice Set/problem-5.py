number = int(input('Enter a number : '))

for i in range(2 , number):
    if(number % 2) == 0:
        print("This is not a PRIME NUMBER")
        break

else:
    print("This is a PRIME Number")