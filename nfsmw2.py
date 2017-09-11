import random
n=(int(input("press 5 to start:")))
while(n==5):
    t=["rock", "paper", "scissor"]
    computer = t[random.randint(0,2)]
    print("enter your choice")
    player = input("rock, paper, scissor?")
    if computer == player:
        print("tie")
    elif player == "rock":
        if computer == "paper":
            print("you lose", computer, "covers", player)
        else:
            print("you win", player, "smashes", computer)
    elif player == "paper":
        if computer == "scissor":
            print("you lose", computer, "cuts", player)
        else:
            print("you win", player, "covers", computer)
    elif player == "scissor":
        if computer == "rock":
            print("you lose", computer, "smashes", player)
        else:
            print("you win", player, "cut", computer)
        
    
