print("Welcome to Yusuf & Sons Ltd".upper().center(80))

principal = float(input("Enter your Principal(₦): "))
rate = float(input("Enter a rate(%): "))
time = float(input("Enter a time(years): "))

simple_interest = "₦" + str((principal * rate * time)/100)

print("Simple Interest = PRT/100 = " + "(" + str(principal) + " × " + str(rate) + " × " + str(time) + ")" + "/100 = " + simple_interest)