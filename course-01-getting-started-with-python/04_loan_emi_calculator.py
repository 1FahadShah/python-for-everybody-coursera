def calculate_emi(pr,ar,t):
    P = pr
    R = ar/12/100 # monthly intereset calculation
    N = t*12 # monthly tenure
    
    EMI = (P * R * (1+R)**N) / ((1+R)**N - 1) # EMI Formula
    
    return EMI

# User Inputs
principal = float(input("Enter loan amount: "))
annual_rate = float(input("Enter Annual Interest Rate: "))
tenure = int(input("Enter Tenure in Years: "))

# EMI calculation
emi = calculate_emi(principal,annual_rate,tenure)
print(f"Your Monthly EMI: Rs.{emi}")
