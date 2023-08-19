# Dictionary: ordered, changeable, does not allow duplicate vales. It uses curly brackets. Here, you use the
# keyword to access an item
'''
car = {
    'brand': "Toyota",
    'model': "camry",
    'year': 2020,
    'brand': "Benz",
    'colour': ['black', 'white', 'grey']
    }
# print(car)
# print(car['model'])
# print(car['colour'])
# 
# x = car.get('colour')
# print(x)

# car['year'] = 2006
car.update({'year': '2006'})
print(car) 
'''
car = {
    'brand': "Lexus",
    'Model': "ES300",
    'brand': "Benz",
    'colour': ['black', 'white', 'grey']
    }
'''
print(car)
print(car['model'])
print(car['colour'])

x = car.get('colour')
print(x)
car['year'] = 2010
'''
car.update({'year': '2010'})
print(car)
