
def Calc_Bmi(height, weight):
    calc = (weight / (height**2)) * 703
    return calc
    
height = float(input("What is your height in inches? "))
weight = float(input("What is your weight in pounds? "))

calc = round(Calc_Bmi(height=height, weight=weight),2)

if calc < 18.5:
    print(f"Your BMI is {calc} you are underweight.")
elif calc >= 18.51 and calc <= 25:
    print(f"Your BMI is {calc} your are a normal weight.")
elif calc >= 25.01 and calc <= 30:
    print(f"Your BMI is {calc} slightly overweight.")
elif calc >= 30.1 and calc <= 35:
    print(f"Your BMI is {calc}, you are obese")
else:
    print(f"You have a BMI of {calc}, you are clinically obese")