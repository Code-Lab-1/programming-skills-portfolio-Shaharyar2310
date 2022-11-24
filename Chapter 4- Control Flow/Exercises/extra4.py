#extra 4
##BMI Calculator
weight = input("Enter weight in kg : ")
height = input("Enter height in cm : ")
b = float(height)**2
BMI = int(weight) / b

if BMI<18.5 :
    print("Underweight")
elif BMI>=18.5 and BMI<25:
    print("Normal")
elif BMI>=25 and BMI<30:
    print("Overweight")
elif BMI>=30:
    print("Obesity")