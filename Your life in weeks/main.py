#https://waitbutwhy.com/2014/05/life-weeks.html
#Another way to look at life...

def main():
    age:int = int(input('How old are you?\n'))
    print("If we suppose that you will die at the age of 90...")
    years_left: int = 90 - age
    days_left:int = years_left*365
    weeks_left:int = years_left*52
    print(f"You have {days_left} days left")
    print(f"You have {weeks_left} weeks left")
    print(f"You have {years_left} years left")



if __name__ == "__main__":
    main()
