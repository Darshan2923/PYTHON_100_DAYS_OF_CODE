print("Welcome here!!!")
bill = float(input("What was the total bill: "))
tip_percent = int(input('Enter tip percentage (10, 20,15): '))
total_bill = bill+bill*tip_percent/100
people = int(input("How many people to split the bill?"))
bill_of_person = round(total_bill/people, 2)
print("Each person should pay ${:.2f}".format(bill_of_person))
