# class Student:

#     def __init__(self , name , marks):
#         self.name = name 
#         self.marks = marks

#     @property
#     def marks(self):
#         return self._marks

#     @marks.setter
#     def marks(self , value):
#         if (value <= 100):
#             self._marks = value
#             print("Number Updated Successfully")
#         else:
#             print("Invalid Marks")

# Student_1 = Student("Zubain" , 80)
# print(Student_1.name)
# print(Student_1.marks)

# Student_1.marks = 500



class UserInfo :
    
    @property
    def name(self):
        return print(self.name)
    
    @name.setter 
    def name(self , value):
        self.f_name = value.split(" ")[0]
        self.l_name = value.split(" ")[1]
        
    
    
e = UserInfo()
e.name = "Zubain Ali"
print(e.l_name)