import time
import random

answer = random.randint(1, 100)
botAnswer = 0
tries = 0

print("The BOT will try guessing a random number that the Computer Generates ")

while(botAnswer != answer):
    botAnswer = random.randint(1, 100)
    time.sleep(0.5)
    print("The bot has guessed: " + str(botAnswer))
    if(botAnswer < answer):
        print("\t The bot should guess a greater number")
        botAnswer = random.randint(botAnswer, 100)
        tries += 1
    elif(botAnswer > answer):
        print("\t The bot should guess a smaller number")
        botAnswer = random.randint(1, botAnswer)
        tries += 1

print()
print("The bot has guessed: " + str(botAnswer))
print("The bot has guessed the answer correctly!")
print("The answer was " + str(answer))
print("The bot has guessed " + str(tries) + " tries")
input()