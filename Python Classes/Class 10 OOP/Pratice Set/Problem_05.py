class Mobile :

    def __init__(self , balance , mobile_name):
        self.balance = balance
        self.mobile_name = mobile_name

    def make_call(self):
        amount = int(input("How much balance do you want to use for a call : "))

        if(amount <= self.balance):
            self.balance -= amount
            print(f'Call Successful ! Amount Charged : {amount}')
            print(f'Your Updated Balance is : {self.balance} ')
        else:
            print(f'Insufficient Balance ! You only have : {self.balance}')

    def recharge(self):
        amount = int(input("How much balance do you want to add : "))
        self.balance += amount
        print(f'Your Updated Balance is : {self.balance}')

    def get_status(self):
        print(f'Your Mobile is : {self.mobile_name}')
        print(f'Your Remaining Balance is : {self.balance}')


user_mobile = input("What is your mobile name : ")
user_mobile = user_mobile.capitalize()

user_1 = Mobile(700 , user_mobile)
user_1.recharge()
user_1.get_status()
user_1.make_call()