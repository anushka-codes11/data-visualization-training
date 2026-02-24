# Read weight (kg) and height (m) from standard input
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

# Validate inputs
if weight <= 0 or height <= 0:
    print("Invalid input")
else:
    # Calculate BMI
    bmi = weight / (height ** 2)

    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        category = "Normal weight"
    elif 25 <= bmi <= 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    # Print BMI and category
    print("BMI:", round(bmi, 2))
    print("Category:", category) 

//  input : 
    Enter weight in kg: 60
    Enter height in meters: 1.7 
//  Output  : 
     BMI: 20.76
     Category: Normal weight     