#Fizzbuzz
#If the number is divisible by 15--> fizzbuzz, divisble by 5--> buzz and divisible by 3 --> fizz or it just prints the number
#At the same time this is leetcode 
#https://leetcode.com/problems/fizz-buzz/
if __name__ == "__main__":
    for number in range(1,101):
        if number % 15 == 0:
            print("fizzbuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(number)

#This is my Leetcode solution:
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        list = []
        for i in range(1,n+1):
            if i % 15 == 0:
                list.append("FizzBuzz")
                continue
            elif i % 5 == 0:
                list.append("Buzz")
                continue
            elif i % 3 == 0:
                list.append("Fizz")
                continue
            else:
                list.append(f"{i}")
        return list
