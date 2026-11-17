total_marks =   int(input("Enter Total Marks : "))

marks = int(input("Enter Obtained Marks : "))


total_percentage = (100 * (marks)) / total_marks 

if(total_percentage >= 90):
    print("Your Grade is EX" , total_percentage)

elif(total_percentage >= 80):
    print("Your Grade is A" , total_percentage)

elif(total_percentage >= 70):
    print("Your Grade is B" , total_percentage)

elif(total_percentage >= 60):
    print("Your Grade is C" , total_percentage)
    
elif(total_percentage >= 50):
    print("Your Grade is D" , total_percentage)
    
elif(total_percentage < 50):
    print("You are Fail" , total_percentage)

else:
    print("Your Entered numbers are not correct")

