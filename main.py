print("                         -------------------------------\n                         | Welcome to Yusuf & Sons Ltd |\n                         ------------------------------".upper())

principal = float(input("Enter your initial amount(₦): "))
interest_rate = float(input("Enter an interest rate(%): "))
n = int(input("Enter number of times interest applied per time period: "))
time = float(input("Enter a time(years): "))

simple_interest = "₦" + str((principal * ( 1 + ( interest_rate * time))))
compound_interest = "₦" + str(principal * (1 + (interest_rate/n)) ** (n * time))

print("\nSimple Interest = P(1 + rt) = " + "(" + str(principal) + "(" + str(1) + " + " + "(" + str(interest_rate) + " × " + str(time) + "))) = " + simple_interest)
print("\nCompound Interest = P(1 + r/n)^nt = " + str(principal) + "(" + str(1) + " + " + "(" + str(interest_rate) + " / " + str(n) + "))" + " ^( " + str(n) + " × " + str(time) + " ) = " + str(compound_interest))