principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
compound_interest = principal * (1 + rate / 100) ** time - principal
print("Compound Interest is:", compound_interest)
