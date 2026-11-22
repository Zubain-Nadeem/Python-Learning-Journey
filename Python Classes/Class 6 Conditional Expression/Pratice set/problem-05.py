list_of_names = ['zubain' , 'qadir' , 'waqas' , 'ahmed']

username = input('Enter your name to see you are eligible for party or not : ')

username = username.lower()


if(username in list_of_names):
    print("you are eligible for party")

else:
    print("you are not eligible for party ")