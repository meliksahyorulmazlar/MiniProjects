#Heads or Tails
#By using the random library, I generate a random number choosing between 0 and 1
#If it is 0 it gets heads and for 1 it gets tails
import random
def coin_flip()->None:
    number:int = random.randint(0,1)
    if number == 0:
        print("Heads")
    else:
        print("Tails")
    
if __name__ == "__main__":
    coin_flip()








