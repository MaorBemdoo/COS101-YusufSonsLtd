print("Welcome to Yusuf & Sons Ltd".upper().center(80))

principal = float(input("Enter your Principal(₦): "))
rate = float(input("Enter a rate(%): "))
time = float(input("Enter a time(years): "))

simple_interest = "₦" + str((principal * rate * time)/100)
compound_interest = "₦" + str((principal * (1 + (rate/100)) ** time) - principal)

print("\nSimple Interest = PRT/100 = " + "(" + str(principal) + " × " + str(rate) + " × " + str(time) + ")" + "/100 = " + simple_interest)
print("\nCompound Interest = P(1+(r/100))-P = " + str(principal) + "(" + str(1) + " + " + "(" + str(rate) + ")" + "/100)" + " - " + str(principal))