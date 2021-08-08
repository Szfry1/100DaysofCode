# BMI calculator that you will input your height and weight and then it will calculate your BMI and tell you if you are over or under weight
weight = float(input("What is your weight ? "))
height = float(input("What is your height ? "))

Bmi_as_int = round(weight / (height ** 2),2)
print(Bmi_as_int)

if Bmi_as_int < 18.5:
    print("You are underweight")
elif Bmi_as_int >= 18.51 and Bmi_as_int <= 25:
    print("You are at a normal weight")
elif Bmi_as_int >= 25.01 and Bmi_as_int <= 30:
    print("Your are slightly overweight")
elif Bmi_as_int >= 30.01 and Bmi_as_int <= 35:
    print("You are obese.")
elif Bmi_as_int > 35:
    print("You are clinically obese.")
