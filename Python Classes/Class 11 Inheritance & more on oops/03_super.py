class Employee:
    def __init__(self):
        print("Employee class is running")
    a = 1

class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Programmer class is running")
    b = 3


o = Programmer()