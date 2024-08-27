import os
import random
os.system("clear")
score1 = 0
score2 = 0

def get_random_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def print_choices(round):
    print("============================")
    print("1: for rock")
    print("2: for Paper")
    print("3: for Scissor")
    print("============================")
    print(f"Enter your choice for round {round}")

def decide_winner(player1,player2):
    global score1,score2,rounds
    if player1 <=3 and player2 <=3:
        if (player1 == player2):
            return 0
        elif (player1==1 and player2==2):
            score2+=1
            return 2
        
        elif (player1==1 and player2==3):
            score1 +=1
            return 1
        
        elif (player1==2 and player2==1):
            score1 +=1
            return 1
        elif (player1==2 and player2==3):
            score2 +=1
            return 2
        
        elif (player1==3 and player2==1):
            score2+=1
            return 2
        
        elif (player1==3 and player2==2):
            score1+=1
            return 1
    else:    
        return 0    

print("Welcome to rock Paper Scissors")
rounds = int(input("Enter the no of rounds you want to play: "))
player_count = int(input("Enter no of players 1 or 2: "))

if player_count == 1:
    
    player1 = input("Enter your name: ")
    player2 =  "computer"
    os.system("clear")
    i = 1
    while i <= rounds:
        print_choices(round=i)
        choice = int(input(f"{player1}: "))
        choicepc = get_random_choice()
        if choicepc=="rock":
            choicepc =1
        elif choicepc=="paper":
            choicepc =2
        elif choicepc=="scissors":
            choicepc =3      
        print(f"PC: {choicepc}")
        result = decide_winner(player1=choice,player2=choicepc)

        if result == 0:
            winner = "Draw"
        elif result == 1:
            winner = player1
        elif result == 2: 
            winner = "Computer"  
        os.system("clear")    
        print(f"Winner for round {i} is : {winner}")
        print("|-------------SCORES--------------|")
        print(f"    machine: {score2} || {player1}: {score1}     ")
        print("|--------------------------------|")
        if winner != "Draw":
            i +=1 
        if ((((int(rounds/2))+1) == score1) or (((int(rounds/2))+1) == score2)):
            i = rounds+1
    os.system("clear")
    print("===========Game Over=============")
    print(f"machine: {score2}")
    print(f"{player1}: {score1}")
    if score2 > score1:
        print(f"Computer wins  by {score2-score1} point/s")
    elif score2 < score1:
        print(f"{player1} wins by {score1-score2} point/s")
    else:
        print("It's a tie")
    print("=================================")

if player_count == 2:
    player1 = input("Enter player1 name: ")
    player2 = input("Enter player2 name: ")
    os.system("clear")
    i = 1
    while i <= rounds:
        
        print_choices(round=i)
        choice1 = int(input(f"{player1}: "))
        os.system("clear")
        print_choices(round=i)
        choice2 = int(input(f"{player2}: "))
        result = decide_winner(player1=choice1,player2=choice2)

        if result == 0:
            winner = "Draw"
        elif result == 1:
            winner = player1
        elif result == 2: 
            winner = player2  
        os.system("clear")    
        print(f"Winner for round {i} is : {winner}")
        print("|-------------SCORES--------------|")
        print(f"    {player1}: {score1} || {player2}: {score2}     ")
        print("|--------------------------------|")
        if winner != "Draw":
            i +=1 
        if ((((int(rounds/2))+1) == score1) or (((int(rounds/2))+1) == score2)):
            i = rounds+1   
    os.system("clear")
    print("===========Game Over=============")
    print(f"{player1}: {score1}")
    print(f"{player2}: {score2}")
    if score2 > score1:
        print(f"{player1} wins  by {score2-score1} point/s")
    elif score2 < score1:
        print(f"{player1} wins by {score1-score2} point/s")
    else:
        print("It's a tie")
    print("=================================")
  
