# value = input('Please enter a value: ')
# print(value)

# import sys
# import random
# from enum import Enum


# class RPS(Enum):
#     ROCK = 1
#     PAPER = 2
#     SCISSORS = 3


# print('')

# playerchoice = input(
#     "Enter...\n1 for Rock 🪨 ,\n2 for Paper, \n3 for scissors ✂️:\n\n")
# player = int(playerchoice)
# if player < 1 | player > 3:
#     sys.exit("You must enter 1, 2, or 3.")
# computerchoice = random.choice("123")
# computer = int(computerchoice)
# print("")
# print("You chose " + playerchoice + ".")
# print("Python chose " + computerchoice + ".")
# print("")
# if player == 1 and computer == 3:
#     print("🥳 You Win!")
# elif player == 2 and computer == 1:
#     print("🥳 You Win!")
# elif player == 3 and computer == 2:
#     print("🥳 You Win!")
# elif player == computer:
#     print("😲 Tie Game!")
# else:
#     print("🐍 Python wins!")


import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# print(RPS(2))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)
# sys.exit()

print('')

playerchoice = input("Enter...\n1 for Rock, \n2 for paper, \n3 for Scissors:\n\n")
player = int(playerchoice)
if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")
computerchoice = random.choice("123")
computer = int(computerchoice)
print("")
print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
print("")
if player == 1 and computer == 3:
    print("🥳 You Win!")
elif player == 2 and computer == 1:
    print("🥳 You Win!")
elif player == 3 and computer == 2:
    print("🥳 You Win!")
elif player == computer:
    print("😲 Tie Game!")
else:
    print("🐍 Python wins!")
