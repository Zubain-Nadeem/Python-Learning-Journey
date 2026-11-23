class Programmer :
    company = "MicroSoft"

    def __init__(self , name , salary , zipcode):
        self.name = name
        self.salary = salary
        self.zipcode = zipcode
    

p = Programmer("Zubain" , 1000000 , 123456)
print(p.name , p.salary , p.zipcode , p.company)