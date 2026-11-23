class Employee:
    name = "Ali"
    salary = 100
    language = "JS"

    def __init__(self , name , salary , language):
        self.name = name
        self.salary = salary
        self.language = language
        


person = Employee("Zubain" , 100000 , "Py")
print(person.name , person.salary , person.language)