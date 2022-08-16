import random
from time import sleep

def game():
    while True:
        User_pick = input("Choose Rock, Paper, or Scissors: ").upper()
        print("Your Pick:" + User_pick)
        AI_pick = ["ROCK", "PAPER", "SCISSORS"]
        random_index = random.randrange(len(AI_pick))
        if User_pick == "ROCK" and AI_pick[random_index]== "PAPER":
            sleep(2.0)
            print("Computer pick:" + AI_pick[random_index])
            sleep(2.0)
            print("YOU LOSE")
            break
        elif User_pick == "ROCK" and AI_pick[random_index]== "SCISSORS":
            sleep(2.0)
            print("Computer pick:" + AI_pick[random_index])
            sleep(2.0)
            print("YOU WIN")
            break
        elif User_pick == "ROCK" and AI_pick[random_index]== "ROCK":
            sleep(2.0)
            print("Computer pick:" + AI_pick[random_index])
            sleep(2.0)
            print("TIE")
            break
        elif User_pick == "PAPER" and AI_pick[random_index]== "PAPER":
            sleep(2.0)
            print("Computer pick:" + AI_pick[random_index])
            sleep(2.0)
            print("TIE")
            break
        elif User_pick == "PAPER" and AI_pick[random_index]== "ROCK":
            sleep(2.0)
            print("Computer pick:" + AI_pick[random_index])
            sleep(2.0)
            print("YOU WIN")
            break
        elif User_pick == "PAPER" and AI_pick[random_index]== "SCISSORS":
            sleep(2.0)
            print("Computer pick:" + AI_pick[random_index])
            sleep(2.0)
            print("YOU LOSE")
            break
        elif User_pick == "SCISSORS" and AI_pick[random_index]== "SCISSORS":
            sleep(2.0)
            print("Computer pick:" + AI_pick[random_index])
            sleep(2.0)
            print("TIE")
            break
        elif User_pick == "SCISSORS" and AI_pick[random_index]== "ROCK":
            sleep(2.0)
            print("Computer pick:" + AI_pick[random_index])
            sleep(2.0)
            print("YOU LOSE")
            break
        elif User_pick == "SCISSORS" and AI_pick[random_index]== "PAPER":
            sleep(2.0)
            print("Computer pick:" + AI_pick[random_index])
            sleep(2.0)
            print("YOU WIN")
            break
        else:
            sleep(2.0)
            print("Invalid Operator")
            sleep(2.0)
            continue

def replay():
    while True:
        Replay = input("Would you like to play again? Yes or No: ").upper()
        if Replay == "YES":
            game()
        elif Replay == "NO":
            break


game()
replay()
