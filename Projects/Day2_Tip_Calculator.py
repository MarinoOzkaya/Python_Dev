print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_as_perc = tip / 100
tip_to_pay = bill * tip_as_perc
bill_after_tip = bill + tip_to_pay
total_pay = bill_after_tip / people
total_pay_rounded = round(total_pay,2)
print(f"Each Person should pay:{total_pay_rounded}")

