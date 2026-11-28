# class Employee:
#     a = 1

#     @classmethod
#     def show(cls):
#         print(f'The Class Attribute a is : {cls.a}')

# e = Employee()
# e.a = 45
# e.show()

class Student:
    school_name = "ABC School"

    def __init__(self , name):
        self.name = name
        print(name)

    @classmethod
    def change_school(cls , new_name):
        cls.school_name = new_name


student_1 = Student("Zubain")
print(student_1.school_name)

student_2 = Student("Ali")
Student.change_school("XYZ School")

print(student_2.school_name)