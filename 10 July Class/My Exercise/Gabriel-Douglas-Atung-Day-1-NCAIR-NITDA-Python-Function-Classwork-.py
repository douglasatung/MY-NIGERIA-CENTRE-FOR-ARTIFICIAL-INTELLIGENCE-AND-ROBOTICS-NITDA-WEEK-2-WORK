#1. CLASSWORK SHOWING AN APPLICANT FILLING A FORM FOR EMPLOYMENT AND IS OFFERED THE JOB
'''
show_employee = ""
name= input("Enter your name: ")
salary= input("Enter enter your envisioned salary: ")
def show_employee(name, salary):
      print('You are hired: ' + name + '. \nCongratulations! Your starting Salary with us will be: ' + salary)
        
show_employee(name,salary)
'''
'''
#2. WE ARE WRITING A PROGRAM REQUEST PATIENTS TO BOOK AN APPOINTMENT WITH THE DOCTOR IN OUR HOSPITAL

show_patient = ""
name_of_patient = input("Enter patient's name: ")
patient_hospital_card_no = input("Enter patient's hospital card number: ")

def show_patient(name_of_patient, patient_hospital_card_no):
    print('Welcome to Destprine Hospital ' + name_of_patient + '. \nYour hospital card number: ' + patient_hospital_card_no + ' is correct')
    
show_patient(name_of_patient,patient_hospital_card_no)
'''

'''
#3. MULTIPLICATION AND DIVISION CALCULATIONS WITH PYTHON
num_1= input('Variable 1 = ')
num_2= input('Variable 2 = ')
Num_1= int(num_1)
Num_2= int(num_2)
def calculation(num_1, num_2):
    multiplication = Num_1 * Num_2
    division = Num_1 // Num_2
    return multiplication, division
print(calculation(Num_1, Num_2))
'''

'''
#4. ADDITION AND SUBTRACTION CALCULATIONS WITH PYTHON
# Assign and input variables
num_1 = input("Variable 1 = ")
num_2 = input("Variable 2 = ")

# Enter Num_1 and Num_2 as integer
Num_1 = int(num_1)
Num_2 = int(num_2)

#defining the x
def calculation(num_1, num_2):
    # Addition of variables
    addition = Num_1 + Num_2
    
    # Subtraction of variables
    subtraction = Num_2 - Num_1
    
    #returning the calculations
    return addition, subtraction
print(Num_1, Num_2)
'''


    