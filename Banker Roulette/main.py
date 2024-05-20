#Banker Roulette
#Concept:
#In real life, a group of bankers come to pay for a meal
#what happens is that the server picks one of the credit cards of the bankers to pay for the ENTIRE meal
#What my code does:
#it asks the person to add the name of the users.
#If someone that has the same exact name is added it puts name with a count
#So if a second John is added, it says John number:2,and if a third John is added, it says John:number 3 and so on
#if you are done adding the users you can input stop
#finally using the random library it will choose someone to pay for the entire meal
import random

def banker_roulette()->None:
    bankers:list = []
    adding_people:bool = True
    while adding_people:
        new_user = input("Write one of the names that will participate in banker roulette and if you have wrote all the names write STOP\n")
        if new_user == "STOP" or new_user.lower() == "stop":
            adding_people = False
        elif new_user in bankers:
            count = bankers.count(new_user) + 1
            new_name = f"{new_user} number:{count}"
            bankers.append(new_name)
        else:
            bankers.append(new_user)
    person_chosen:str = random.choice(bankers)
    print(f"{person_chosen} was chosen to pay for the entire meal!")


if __name__ == "__main__":
    banker_roulette()










