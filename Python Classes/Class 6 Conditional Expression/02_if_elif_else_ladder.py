user = int(input("Enter Your Age : "))

if (user > 20):
    print('You are eligible')

elif(user < 0):
    print("You are entering the invalid age ")

elif(user == 0):
    print("You cannot write Zero")

else:
    print("You are not eligible")


