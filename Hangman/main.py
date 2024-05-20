#Hangman
#What my code does is it opens a text file(the user can edit the contents of the text file as they like to add or remove words)
#it makes an output of the number of letters in that word.If there are 5 letters it prints out _____
#There are 2 difficulties easy and hard.Easy has 5 lives and hard has 10 lives
#when the game starts it asks for a letter if the user accidentally types 2 letters nothing happens
#if the letter is in the word,now onwards the screen will replace the _ with the letter
#if the user types a letter that has been already said it will have no effect on the users lives
#if the user accidentally types a punctuation symbol,number etc. it will have no effect on the user's lives
#if there are no _ left on the screen(the user found all the letters) the user has won
#if the user has no more lives it will show the word



if __name__ == "__main__":
    import random
    with open("words.txt","r") as r:
        words:list = r.readlines()
        words:list = [word.replace("\n","") for word in words]
    word:str = random.choice(words)

    letters:list = [letter for letter in word]
    letter_list:list = []
    for i in range(len(word)):
         letter_list += "_"

    screen:str = "".join(letter_list)

    used_letters:list = []
    lives:int = 5
    difficulty:str = input("What difficulty would you like to play this game?\nType easy or hard\n")
    if difficulty.lower() == "easy":
        lives:int = 10
    print(screen)
    while lives !=0:
        letter:str = input("Enter a letter").lower()
        if len(letter) == 1:
            if letter in letters and letter not in used_letters:
                for i in range(len(word)):
                    if word[i] == letter:
                        letter_list[i] = letter
                        screen = "".join(letter_list)
                        print(screen)
                    if "_" not in letter_list:
                        print("You won!")
                        exit()
            elif letter in used_letters:
                pass
            else:
                if letter.isalpha():
                    used_letters.append(letter)
                    screen = "".join(letter_list)
                    print(screen)
                    print(f"{letter} is not in the word")
                    lives -= 1
                else:
                    pass
        else:
            pass
    print(f"You lost the word was {word}")