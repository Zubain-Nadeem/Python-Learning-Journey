class Book:

    def __init__(self , book_name , price):
        self.book_name = book_name
        self.price = price
        
    def __add__(self, other):
        return self.price + other.price
    
    def __sub__(self, other):
        return self.price - other.price
    
    def __mul__(self, other):
        return self.price * other.price
    
    def __truediv__(self, other):
        return self.price / other.price
    
    

person = Book("Math" , 900)
person_1 = Book("PAk" , 799)


print(f'Addition: {person + person_1}') 
print(f'Sub: {person - person_1}')
print(f'Multiply: {person * person_1}')
print(f'Division: {person / person_1}')