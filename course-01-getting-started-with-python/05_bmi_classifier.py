def bmi_classify(bmi):
    if bmi < 18.5:
        return "Underweight :("
    elif bmi < 25:
        return "Normal :)"
    elif bmi < 30:
        return "Overweight!!! :>"
    else:
        return "obese"

def get_height_in_meters():
    print("Select Method: ")
    print("1. Centimeter")
    print("2. Feet and Inches")
    method = int(input("Enter 1 or 2: "))
    if method == 1:
        height_cm = float(input("Enter Height in Centimeter: "))
        return height_cm/100
    elif method == 2:
        foot = int(input("Enter Foot: "))
        inches = int(input("Enter Inches: "))
        total_inches = foot*12 + inches
        return total_inches * 0.0254
    else:
        print("Enter Valid Choice!!!")
        exit()

weight_kg = float(input("Enter Weight in KG: "))
height_m = get_height_in_meters()

bmi = weight_kg/height_m**2

print(f"Your BMI: {bmi}")
print(f"Category: {bmi_classify(bmi)}")

