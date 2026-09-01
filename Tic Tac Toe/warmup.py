game_list = [1,2,3]

def display_list(game_list):
    print("This is the current list")
    print(game_list)


def user_choice():
    choice = ""

    while choice not in ['0','1','2']:
        choice = input("Enter a position from (0,1,2): ")
        if choice  not in ['0','1','2']:
            print("Sorry you have entered the wrong position ")

    return int(choice)


def replacement_choice(game_list,position):
    user_placement = input("Type of string you want to place: ")
    game_list[position] = user_placement
    return game_list

def game_on_choice():

    choice = ""

    while choice not in ['Y','N']:
        choice = input("Enter Y/N to continue the game: ")
        if choice not in ['Y','N']:
            print("Choose the correct option ")

    if game_on_choice == "Y":
        return True
    else:
        return False

#initialize 
game_on= True

while game_on:
    display_list(game_list)

    position = user_choice()

    game_list = replacement_choice(game_list,position)

    display_list(game_list)

    game_on = game_on_choice()