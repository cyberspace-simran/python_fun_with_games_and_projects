import random

def game_win(comp ,  player):
    # If computer and player get same value its a tie 
    if comp == player :
        return None
    elif comp == "r":
        if player == "s":
            return False
        elif player == "p":
            return True
    elif comp == "s":
        if player == "p":
            return False
        elif player == "r":
            return True
    elif comp == "p":
        if player == "s":
            return False
        elif player == "r":
            return True

print("Computer turn: Rock(r) Paper(p) scissior(s)?")
randNo = random.randint(1 , 3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp =  'p'
elif randNo == 3:
    comp =  's'

player = input ("Your turn: Rock(r) Paper(p) scissior(s)?")

c = game_win(comp , player )


print(f"computer chose {comp}")
print(f'player chose {player}')


if  c == None:
    print("Match is draw!")
elif c:
    print("You win")
else:
    print("You Lose")            