#Buzzfeed Love Calculator
#https://www.buzzfeed.com/ariannarebolini/what-are-the-chances-your-crush-is-actually-your-true-love

def calculate_love(name1:str,name2:str) -> None:
    both_names:str = name1.lower()+name2.lower()
    t:int = both_names.count("t")
    r:int = both_names.count("r")
    u:int = both_names.count("u")
    e:int = both_names.count("e")
    l:int = both_names.count("l")
    o:int = both_names.count("o")
    v:int = both_names.count("v")
    first:str = str(t+r+u+e)
    second:str = str(l+o+v+e)
    total:int = int(first+second)
    if total < 10 or total > 90:
        print(f"Your score is {total}, you go together like coke and mentos.")
    elif total > 40 and  total < 50:
        print(f"Your score is {total}, you are alright together.")
    else:
        print(f'Your score is {total}')


if __name__ == "__main__":
    print("Welcome to the Buzzfeed Love Calculator!")
    first_person = input("Enter the name of the first person\n")
    second_person = input("Enter the name of the second person\n")
    calculate_love(first_person,second_person)

