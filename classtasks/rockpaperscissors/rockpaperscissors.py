import random


def main():
    playerchoice = str(input("rock paper scisors"))
    choices = ["rock", "paper", "scissor"]
    x = random.choice(choices)
    match playerchoice:
        case "rock":
            if x == str("paper"):
                print("you lose")
            elif x == str("rock"):
                print("you tie")
            elif x == str("scissor"):
                print("you win")
            else:
                print("nothing")
        case "paper":
            if x == str("paper"):
                print("you tie")
            elif x == str("rock"):
                print("you win")
            elif x == str("scissor"):
                print("you lose")
            else:
                print("nothing")
        case "scissor":
            if x == str("paper"):
                print("you win")
            elif x == str("rock"):
                print("you lose")
            elif x == str("scissor"):
                print("you tie")
            else:
                print("nothing")


main()
