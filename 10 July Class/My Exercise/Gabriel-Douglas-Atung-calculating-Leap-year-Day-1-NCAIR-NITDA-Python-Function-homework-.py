'''
#WRITING A PYTHON PROGRAM TO CHECK IF YEAR IS A LEAP YEAR OR NOT

def checkyear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
year = int(input("Enter a year of your choice: "))
if (checkyear(year)):
    print("The year is a leap year")
else:
    print("The year is not a leap year")
'''


def checkyear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
year = int(input("Enter a year of your preference: "))
if (checkyear(year)):
    print("The year entered is a leap year")
else:
    print("The year entered is not a leap year")
