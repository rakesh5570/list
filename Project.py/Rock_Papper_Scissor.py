import random
from time import sleep


def game():
    user= input("Your choice-> 'r' for rock, 'p' for papper, 's' for scissor\n")
    computer=random.choice(['r','p','s'])

    sleep(2)

    if user==computer:
        return "Its tie......"

    if is_win(user, computer):
        return "You Win waoo......."
    
    return "You loose......huhh -> 'Try again'"


def is_win(player, opponent):
    if (player=='r' and opponent=='p') or (player=='p' and opponent=='s') or (player=='s' and opponent=='r'):
        return True

print(game())