class Student:
    def __init__(self , name , rollno , clas , marks):
        self.name = name
        self.rollno = rollno
        self.clas = clas
        self.marks = marks

    def get_details(self):
        print(f'Student Name : {self.name}')
        print(f'Student Roll no : {self.rollno}')
        print(f'Student Class : {self.clas}')

    def get_marks(self):
        print(f'Student Marks : {self.marks}')

    def get_result(self):
        if (self.marks >= 40):
            print("Student is Passed!")
        else:
            print("Student is Failed!")


number = int(input("Enter your number out of 100 : "))
student_1 = Student("Zubain" , 12 , 10 , number)
student_1.get_details()
student_1.get_marks()
student_1.get_result()


class BankAccount :

    def __init__(self , balance):
        self.balance = balance

    def deposit(self):
        amount = int(input("Enter Deposit Amount : "))
        self.balance += amount
        print("Deposit Successfully !")
        print(f'Your Updated Balance is : {self.balance}')

    def withdraw(self):
        amount = int(input("Enter WithDraw Amount : "))

        if (amount <= self.balance):
            self.balance -= amount
            print(f"Your WithDraw : {amount}")
            print(f'Your Remaining Balance is : {self.balance}')
        else:
            print(f'insufficient Balance')

    def  check(self):
        print(f'Your Current Balance is : {self.balance}')


person_1 = BankAccount(5000)
person_1.deposit()
person_1.withdraw()
person_1.check()
