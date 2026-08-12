import random, sys
#we imported the random and sys module to use the random.randint() and sys.exit() function 

print("ROCK, PAPER, SCISSORS")

#display and keeps track of the wins,losses and ties
wins = 0
losses = 0 
ties = 0

while True: #the main loop
    print("%s wins, %s losses, %s ties" %(wins,losses,ties))
    while True:
        player_move=input("Rocks(r),papers(p),Scissors(s) or quit(q): ")
        if player_move == "q":
            sys.exit()
        if player_move == 'r' or player_move == "p" or player_move == "s":
            break
        print("choose any one not all")
        
    #display palyer move
    if player_move == "r":
        print("ROCK versus...")
    elif player_move == "s":
        print("SCISSORS versus...")
    elif player_move == "p":
        print("PAPER...")

    #display computer moves
    move_number=random.randint(1,3)

    if move_number==1:
        computer_move ="r"
        print("ROCK")
    elif move_number==2:
        computer_move = "s"
        print("SCISSOR")
    elif move_number ==3:
        computer_move = "p"
        print("PAPER")

    #the game rules and diplay the wins,losses and ties
    if player_move == computer_move:
        print("its a tie")
        ties += 1
    elif player_move == 'r' and computer_move== 's':
        print("you win")
        wins += 1
    elif player_move == 'p' and computer_move == 'r':
        print("you win")
        wins +=1
    elif player_move == 's' and computer_move == 'p':
        print("you win")
        wins +=1
    elif player_move == 'r' and computer_move == 'p':
        print("you lose")
        losses +=1
    elif player_move == 's' and computer_move == 'r':
        print("you lose")
        losses +=1
    elif player_move == 'p' and computer_move == 's':
        print("you lose")
        losses +=1
