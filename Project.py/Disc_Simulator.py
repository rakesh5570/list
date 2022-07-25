# Random number occurance in dice



import random
from time import sleep


min_val=1
max_val=6

roll_again=str(input("Roll the disc1->"))

while roll_again=="yes" or roll_again=="y" :
    print("Disc is rolling.........")
    sleep(2)
    print("Your lucky value is->")
    sleep(3)
    print(random.randint(min_val,max_val))
    break
    

# roll_again1=str(input("Roll the dice2->"))
