import random

def game():
    print("You are playing game")
    score = random.randint(1 , 100)
    with open("hiscore.txt") as f:
        hi_score = f.read()
    
        if(hi_score != ""):
            hi_score = int(hi_score)
        else:
            hi_score = 0
            
    
    if (score > hi_score):
        with open("hiscore.txt" , "w") as f :
            f.write(str(score))
    
    print(f"Your Score is : {score}")
    
    return score


game()
        