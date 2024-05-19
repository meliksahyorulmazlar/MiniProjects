#This checks if a year is a leap year or not
#If it is not divisible by 4 it is not a leap year
#if it is divisible by 4 and 400 then it is a leap year(1200,1600,2000 are leap years)
#but if it is divisible by 4 and 100 (1700,1800,1900) it is not a leap year
#if all other conditions are false then it is a leap year 2004,2008,2012,2016,2020,2024 and so on

def leap_year(year:int)->bool:
    if year % 4 != 0:
        return False
    elif year % 4 ==0 and year % 400 == 0:
        return True
    elif year % 4 ==0 and year % 100 == 0:
        return False
    else:
        return True


if __name__ == "__main__":
    year: int = int(input("Enter a year to check if it is a leap year or not"))
    result = leap_year(year)
    if result == True:
        print(f"{year} was a leap year")
    else:
        print(f"{year} was not a leap year")

