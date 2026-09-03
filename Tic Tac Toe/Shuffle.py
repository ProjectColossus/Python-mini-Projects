#Mini Project Warmup
#first you use the random module to call the shuffle
from random import shuffle 

#then u initialize a list of the shuffling game!
mylist = [' ','O',' ']

#you define a function to shuffle the mylist
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

#you take the player guess: 
#1 Initalize a Empty string 
#2 Take the guess in string nd then return in int 
def player_guess():
    guess =""

    while guess not in ['0','1','2']:
        guess = input("Enter a Number from 0,1 or 2: ")
    return int(guess)

# in the check guess function we want the mylist to take the index part, which is why we converted guess to int
def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("Correct")
        print(mylist)
    else:
        print("Wrong Guess")
        print(mylist)


#initial List
mylist = [' ','O',' ']
#Shuffle it
mixed_list = shuffle_list(mylist)
#get guess
guess = player_guess()
#Check the guess is right or wrong
check_guess(mixed_list,guess)


