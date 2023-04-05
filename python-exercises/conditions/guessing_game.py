from random import randint
computer = randint(0,5)
print("I'll think of a number between 0 and 5. Try to guess...")
player = int(input("What number did i think of ? "))
if player == computer:
    print("Congratulations!You managed to beat me!")
else:
    print(f"I won!I thought of the number {computer} and not {player}.")