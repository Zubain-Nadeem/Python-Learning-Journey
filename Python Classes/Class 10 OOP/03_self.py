class Employee :
    name = "Zubain"
    salary = 100000
    language = "Py"

    def getinfo(self):
        print(f'The Language is {self.language} and the salary is {self.salary}')

    def greet(self):
        print("Good Morning")

    @staticmethod
    def greet_2():
        print("Hello !")

person = Employee()

person.getinfo()
person.greet()
person.greet_2()
# Employee.getinfo(person)