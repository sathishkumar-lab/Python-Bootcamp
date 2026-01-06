print("\n\n\t\t\t\033[1m Welcome to tip calculator! \033[0m")
bill=int(input("\n Enter the total bill : "))
tip=int(input("\n How much tip would you like to give? 5, 7, 10 : "))
member=int(input("\n How many member do you want to split : "))
total_bill=(bill+(bill*tip/100))/member
print("\n Total amount each should pay is : ", total_bill)