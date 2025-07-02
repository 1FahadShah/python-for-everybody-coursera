def grade(a):
    if a>100 or a<0:
        return "Please Enter between 0-100"
    elif score >= 90:
        return "Grade A"
    elif score >= 80:
        return "Grade B"
    elif score >= 70:
        return "Grade C"
    elif score >= 60:
        return "Grade D"
    elif score >= 50:
        return "Grade E"
    else:
        return "Fail"

score_input = input("Enter Score (0-100): ")
if score_input.isdigit():
    score = float(score_input)
    print(grade(score))
else:
    print("Please Enter valid number")
