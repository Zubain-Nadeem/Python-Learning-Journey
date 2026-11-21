import random

computer = random.randrange(1 , 4)
user = input("Enter The Alphabet : R for Rock : P for Paper : S for Scissors : ")
user = user.lower()

r_p_s_dict = {
    "r" : 1,
    "p" : 2 ,
    "s" : 3
}

reversed_r_p_s_dict = {
    1 : "Rock",
    2 : "Paper",
    3 : "Scissors"
}

user_pick = r_p_s_dict[user]


if (user_pick == 1 and computer == 3):
    print(f'You Won ! Your Pick {reversed_r_p_s_dict[user_pick]} and Computer Pick {reversed_r_p_s_dict[computer]}')

elif (user_pick == 2 and computer == 1):
    print(f'You Won ! Your Pick {reversed_r_p_s_dict[user_pick]} and Computer Pick {reversed_r_p_s_dict[computer]}')

elif (user_pick == 3 and computer == 2):
    print(f'You Won ! Your Pick {reversed_r_p_s_dict[user_pick]} and Computer Pick {reversed_r_p_s_dict[computer]}')

elif (user_pick == computer):
    print(f'Its Draw ! Your Pick {reversed_r_p_s_dict[user_pick]} and Computer Pick {reversed_r_p_s_dict[computer]}')  

else:
   print(f'You Lost ! Your Pick {reversed_r_p_s_dict[user_pick]} and Computer Pick {reversed_r_p_s_dict[computer]}')  
