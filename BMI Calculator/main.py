#Metric System for the BMI calculator (Body mass index)

def bmi_calculate(weight:float,height:float)->None:
  #The way you calculate bmi is the weight in kilograms divided by the height in meters to the power of 2
  bmi:float = weight/pow(height,2)
  state = ""
  if bmi < 18.5:
    state = "underweight"
  elif bmi > 18.5 and bmi < 25:
    state = 'normal weight'
  elif bmi > 25 and bmi < 30:
    state = "slightly overweight"
  elif bmi > 30 and bmi < 35:
    state = "obese"
  else:
    state = "clinically obese"
  print(f"Your bmi is {bmi:.2f} to 2 decimal places and you are considered to be {state} according to this bmi data given")



if __name__ == "__main__":
  print("Welcome the BMI calculator")
  user_weight = float(input("How much is your weight in kilograms\n"))
  user_height = float(input("How much is your height in meters (100 cm = 1 meter)\n"))
  bmi_calculate(user_weight, user_height)
  
