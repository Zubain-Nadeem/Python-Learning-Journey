#Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.


total_marks = 300 

subject_1_marks = int(input("Enter Subject 1 Marks : "))
subject_2_marks = int(input("Enter Subject 2 Marks : "))
subject_3_marks = int(input("Enter Subject 3 Marks : "))


total_percentage = (100 * (subject_1_marks + subject_2_marks + subject_3_marks)) / total_marks 

if(total_percentage >= 40 and subject_1_marks >= 33 and subject_2_marks >= 33 and subject_3_marks >= 33):
    print("You are Passed" , total_percentage)

else:
    print("You are Fail" , total_percentage)

