# class Employe :
#     name = "Zubain"
#     salary = 100000
#     language = "PYTHON"

# person = Employe()
# print(person.name , person.salary , person.language)

class Employe :
    salary = 100000 #This is a class attribute
    language = "PYTHON"

zubain = Employe()
zubain.name = 'Zubain' #This is an instance attribute

print(zubain.name , zubain.salary , zubain.language)

# here name is the instance attribute and salary and language are the class attribute as they dirctly bleong to the class