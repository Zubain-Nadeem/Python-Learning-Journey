class Student:

    def __init__(self , name , marks):
        self.name = name
        self.marks = marks

    @property

    def result(self):
        if (self.marks >= 40):
            print("Pass")
        else:
            print("Fail")


student_1 = Student("Zubain" , 89)
student_1.result