class Employe :
    name = "Zubain"
    salary = 100000
    language = "Py"

person = Employe()
person.language = "JS"

print(person.language)


# Note: Instance attributes, take preference over class attributes during assignment &
# retrieval.
