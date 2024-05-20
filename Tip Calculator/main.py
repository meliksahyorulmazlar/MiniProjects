#Tip Calculator
#The code gets the cost of the meal and then asks what percentage of a tip would you like to give
#Then the code asks how many people will be paying for the meal and divides the cost equally among them
#Finally the code tells how much how the meal will cost with the tip and how much each person will pay

def calculate_tip(cost:float,percent:float,number:int)->None:
    new_cost:float = ((percent/100)*cost)+cost
    per_person:float = new_cost/number
    print(f"The new total cost is {new_cost:.2f}")
    print(f"The total cost per person is {per_person:.2f}")



if __name__ == "__main__":
    bill:float = float(input("How much did the meal cost\n"))
    percentage:float = float(input("What percentage of a tip would you like to give(Don't include the percentage sign)\n"))
    count:int = int(input("How many people will be paying for the meal\n"))
    calculate_tip(bill,percentage,count)







