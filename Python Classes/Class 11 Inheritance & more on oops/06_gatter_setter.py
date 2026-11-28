class Student:

    def __init__(self , name , marks):
        self.name = name 
        self.marks = marks

    @property
    def marks(self):
        return self.marks

    @marks.setter
    def marks(self , value):
        if (self.marks <= value <=100):
            print("Number Updated Successfully")
        else:
            print("Invalid Marks")

Student_1 = Student("Zubain" , 80)
Student_1.marks