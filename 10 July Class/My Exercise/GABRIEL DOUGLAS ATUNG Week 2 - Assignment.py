#1. Writing a code for a custoer ordering pizza with options of adding extra pepperoni and cheese
'''
#Assignment Week 2
# Build an automated Pizza order program
print("welcome to NITDA Pizza Deliveries!")
size = input("What size of pizza do you want?, S, M, or L ")
add_pepperoni  = input("Do you want pepperoni? Yes or No ")
extra_cheese = input("Do you want extra cheese? Yes or No ")
bill = 0
if size == "S":
    bill += 15
elif size =="M":
    bill += 20
elif size == "L":
    bill += 25

if add_pepperoni == "Yes":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Yes":
    bill += 1

print(f"Your final bill is ${bill}")
'''

#2. Writing a code for a customer ordering yam with additional pomo and fish
#Welcoming our customer 
print("Welcome to Destprine Food Ltd!")

#Asking the customer the variety of food he/she may want
size = input("What size of yam will you like to order?, S, M or L: ")
adding_pomo = input("Will you like to add pomo? Yes or No: ")
adding_fish = input("Will you like to add fish too? Yes or No: ")

amount = 0

if size=="S":
    amount += 20
elif size== "M":
    amount += 30
elif size == "L":
    amount += 40
    
if adding_pomo == "Yes":
    if size == "S":
        amount += 5
    else:
        amount += 7
if adding_fish == "Yes":
    amount += 4
print(f"Your total amount is ${amount}")