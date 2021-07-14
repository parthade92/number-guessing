import random

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""


def hard():
    for i in range(5, 0, -1):
        print(f"You have {i} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == comp_number:
            print(f"You got it! The answer was {comp_number}")
            break
        elif guess < comp_number:
            print("Too Low")
        elif guess > comp_number:
            print("Too High")
        if i == 1:
            print("You've lost")



def easy():
    for i in range(10, 0, -1):
        print(f"You have {i} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == comp_number:
            print(f"You got it! The answer was {comp_number}")
            break
        elif guess < comp_number:
            print("Too Low")
        elif guess > comp_number:
            print("Too High")
        if i == 1:
            print("You've lost")


def choice():
    flag = 'yes'
    while flag == 'yes':
        c = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if c == 'easy':
            easy()
        else:
            hard()
        flag = input("Do you want to continue? 'yes' or 'no':").lower()


print(logo)
print("Welcome to the number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
comp_number = random.randint(1, 101)
choice()


