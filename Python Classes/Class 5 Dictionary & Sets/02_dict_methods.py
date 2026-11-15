marks = {
    "Ali" : 89,
    "Quioere" : 22 ,
    "Zubain" : 100 
}

print(marks.items()) # Return result in key value pair in a form of tuples
print(marks.keys()) # Return Keys Name 
print(marks.values()) # Return Values of Keys 
marks.update({"Zubain" : 99 , "John" : 78})
print(marks)
print(marks.get("Zubain"))