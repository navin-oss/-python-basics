weight=float(input("Enter the weight in kg="))
height=float(input("Enter the height in meter="))
BMI=round(weight//(height**2))
print(BMI)
if BMI<18.5:
    print(f"Your BMI is {BMI} and you are under wieght.")
elif  35>BMI>=25:
    print(f"Your BMI is {BMI} and you are over wieght.")
elif 18.5<BMI<24.9:
    print(f"Your BMI is {BMI} and you are noraml range")
elif BMI<35:
    print(f"Your BMI is {BMI} and you are obese.")
else:
    print(f"Your BMI is {BMI} and you are clinically not good.")