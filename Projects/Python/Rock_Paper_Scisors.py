import random
def gameWin(comp, you):
    if comp == you:
        return None
    if comp == 'r':
        if you == 's':
            return False
        if you == 'p':
            return True
    if comp == 'p':
        if you == 'r':
            return False
        if you == 's':
            return True
    if comp == 's':
        if you == 'p':
            return False
        if you == 'r':
            return True


print("Computer's turn: Rock(r), Paper(p) or Scisors(s)?")
randNo = random.randint(1, 3)

if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you = input("Your turn: Rock(r), Paper(p) or Scisors(s)? ")
a = gameWin(comp, you)

if a == None:
    print('Game is a tie')
elif a:
    print("You win")
else:
    print('You loose')
print(f"Computer chose : {comp}")
print(f"You chose : {you}")
