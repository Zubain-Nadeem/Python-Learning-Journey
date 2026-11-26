# class Student:
#     def __init__(self , name , rollno , clas , marks):
#         self.name = name
#         self.rollno = rollno
#         self.clas = clas
#         self.marks = marks

#     def get_details(self):
#         print(f'Student Name : {self.name}')
#         print(f'Student Roll no : {self.rollno}')
#         print(f'Student Class : {self.clas}')

#     def get_marks(self):
#         print(f'Student Marks : {self.marks}')

#     def get_result(self):
#         if (self.marks >= 40):
#             print("Student is Passed!")
#         else:
#             print("Student is Failed!")


# number = int(input("Enter your number out of 100 : "))
# student_1 = Student("Zubain" , 12 , 10 , number)
# student_1.get_details()
# student_1.get_marks()
# student_1.get_result()

initial_balance = 5000

class BankAccount :
    def __init__(self , user_deposite , user_withdraw):

        self.user_deposite = user_deposite
        self.user_withdraw = user_withdraw
       

    def deposit(self):
        self.user_deposite = int(input("Enter Your Deposite Amount : "))
        self.user_deposite += initial_balance
        print(f'Your Updated Balance is : {initial_balance}')

    def check_blance(self):
        print(f'Your Current Balance is : {initial_balance}')

    def with_draw(self):
        self.user_withdraw = int(input("Enter Your With Drawl Amount : "))
        self.user_withdraw -= initial_balance
        print(f'Your With Draw Amount : {self.user_withdraw}')     
        print(f'Your Remaing Balance is : {initial_balance}')


            
person_1 = BankAccount()
person_1.deposit()
