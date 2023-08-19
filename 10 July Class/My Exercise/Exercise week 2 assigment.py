print("WELCOME TO TOPMOST PIZZA TERRAIN")
response = input("HOW ARE YOU?: ")
size = input("What size of our pizza will you love to have?, S, M, or L ")
add_pepperoni = input("Will you like additional pepperoni?, Yes or No? ")
add_cheese = input("Will you like additional cheese?, Yes or No? ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if add_pepperoni == "Yes":
    if size == "S":
        bill += 2
    else:
        bill += 3
if add_cheese == "Yes":
    bill += 1
    
print(f"Your total bill is ${bill}")