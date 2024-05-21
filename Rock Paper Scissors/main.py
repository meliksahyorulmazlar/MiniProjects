#Rock Paper Scissors
#using the random library
#It will ask the user for an input.0 for rock,1 for paper and 2 for scissors
#if the user does not input those, it will again ask for an input
#the code using the random library will choose a number between 0 and 2 inclusive
#if both the computer and the user put the same, the game ends in a draw
#then I made a dictionary where it shows the win cases  for the particular input from user
#so what the code will do is the code will check the dictionary where the users input will be the key and if the value is equal to the computers choice
#If it is equal it will say that the user won or else it will say that the user lost




import random

def play(user_input:int)->None:
    computers_choice:int = random.randint(0,2)
    user_win_cases:dict[int,int] = {1:0,2:1,0:2}
    options: dict = {'0': "rock", "1": "paper", "2": "scissors"}
    print(f"The computer chose {options[str(computers_choice)]}")
    if computers_choice == users_choice:
        print("Draw")
    else:
        if user_win_cases[user_input] == computers_choice:
            print("You won")
        else:
            print("You lost")



if __name__ == "__main__":
    options:dict[str,str] = {'0':"rock","1":"paper","2":"scissors"}
    game_works:bool = True
    while game_works:
        users_choice:str = input("enter 0 for rock, enter 1 for paper and 2 for scissors\n")
        if users_choice in options:
            print(f"You chose {options[users_choice]}")
            users_choice:int = int(users_choice)
            play(users_choice)
            game_works:bool = False









