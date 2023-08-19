# num_1= input('Variable 1 = ')
# num_2= input('Variable 2 = ')
# num_3= input('Variable 3 = ')
# Num_1= int(num_1)
# Num_2= int(num_2)
# Num_3= float(num_3)
# def calculation(num_1, num_2, num_3):
#     addition = Num_1 + Num_2
#     subtraction = Num_1 - Num_2
#     multiplication = Num_3 * Num_2
#     return addition, subtraction, multiplication
# print(calculation(Num_1, Num_2, Num_3))

'''
#Calculating the total money realised after sales of day 1
num_1 = input('Figure 1 = ')
num_2 = input('Figure 2 = ')
num_3 = input('Figure 3 = ')
num_4 = input('Figure 4 = ')
Num1 = int(num_1)
Num2 = float(num_2)
Num3 = int(num_3)
Num4 = bool(num_4)
def calculation(num_1, num_2, num_3, num_4):
    addition = Num2 + Num1
    subtraction = Num2 - Num1 
    multiplication = Num3 * Num2 >= Num4
    return addition, subtraction, multiplication
print(calculation(Num1, Num2, Num3, Num4))
'''

#Write a program showing whether a code various output int int, float and boolean
num_1 = input('First Entery = ')
num_2 = input('Second Entry = ')
num_3 = input('Third Entry = ')
num_4 = input('Fourth Entry = ')

Nm_1 = int(num_1)
Nm_2 = float(num_2)
Nm_3 = bool(num_3)
Nm_4 = float(num_4)

def calculations(num_1, num_2, num_3, num_4):
    addition = Nm_1 + Nm_4 != Nm_2
    multiplication = Nm_2 * Nm_1
    subtraction = Nm_4 - Nm_2
    return addition, multiplication, subtraction
print(calculations(Nm_1, Nm_2, Nm_3, Nm_4))