import random

def game():
    print("You are playing a game ")
    score=random.randint(1,62) 
    with open("hiscore.txt") as f:
        highscore=f.read()
    if(highscore!=""):
        highscore=int(highscore)
    else:
        highscore=0
    print(f"Your Score {score}")
    if(score>highscore):
        with open("hiscore.txt","w") as f:
            f.write(str(score))
    


game()
