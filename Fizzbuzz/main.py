#Fizzbuzz
#If the number is divisible by 15--> fizzbuzz, divisble by 5--> buzz and divisible by 3 --> fizz or it just prints the number

if __name__ == "__main__":
    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(number)