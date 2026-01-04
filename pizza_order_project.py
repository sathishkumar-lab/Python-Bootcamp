"""
Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill. Use the input() function to get a user's preferences and then add up the total for their order and tell them how much they have to pay.
Small pizza (S): $15
Medium pizza (M): $20
Large pizza (L): $25
Add pepperoni for small pizza (Y or N): +$2
Add pepperoni for medium or large pizza (Y or N): +$3
Add extra cheese for any size pizza (Y or N): +$1
Example Interaction
Welcome to Python Pizza Deliveries!
What size pizza do you want? S, M or L: L
Do you want pepperoni on your pizza? Y or N: Y
Do you want extra cheese? Y or N: N
Your final bill is: $28.
"""

print("Welcome to Python Pizza Deliveries!")
size=input("What size of pizza do you want? S, M, or L : ")
if size=="S":
    prize=int(15)
elif size=="M":
    prize=int(20)
elif size=="L":
    prize=int(25)
else:
    print("You have choosen an invalid size")

pepperoni=input("Do you want pepperoni on your pizza? Y or N : ")
if pepperoni=="Y":
    if size=="S":
        prize+=2
    else:
        prize=+3
cheese=input("Do you want extra cheese? y or N : ")
if cheese==Y:
    prize+=1
print("your final bill is : $",prize)