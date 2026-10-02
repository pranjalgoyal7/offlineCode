import random  #imports random module


def gameWin(comp, you):
    if comp == you:  #if both are equal, it returns noe
        return None

    if comp == 's':  # if computer chooses snake, it will check the following posiblities
        if you == 'w':
            return False  # if we chose water we loose
        elif you == 'g':
            return True  # if we chose gun we win

    elif comp == 'w':  # if computer chooses water, it will check the following posiblities
        if you == 'g':
            return False  #if we chose gun we loose
        elif you == 's':
            return True  # if we chose snake we win

    elif comp == 'g':  #if computer chooses gun, it will check the following posiblities
        if you == 's':
            return False  # if we chose snake we loose
        elif you == 'w':
            return True  # if we chose water we win


print("Computer Turn : snake, water or gun?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your turn: snake(s), water(w) or gun(g)? ")
print(f"Computer chose {comp}")
print(f"You chose {you}")

a = gameWin(comp, you)
if a == None:
    print('Game is a tie')
elif a:
    print("You win")
else:
    print('You loose')