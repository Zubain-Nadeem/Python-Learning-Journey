class Calculator :

    def __init__(self , number):
        self.number = number

    def square(self):
        print(f'The Square is {self.number * self.number}')

    def cube(self):
        print(f'The Cube is {self.number * self.number * self.number}')  

    def squareroot(self):
        print(f'The Square Root is {self.number ** 0.5}')


number = int(input("Enter your number to find square , cube and square root : "))

n = Calculator(number)
n.square()
n.cube()
n.squareroot()