#calling funtiions
# def my_function (first_name):
#     print(first_name + ' Atung')
#     
# my_function('Ninyio')
# my_function('Ndow')
# my_function('Chaayan')
# my_function('Yashim')

# def my_function(first_name, last_name):
#     print(first_name + ' ' + last_name)
# 
# my_function('Ninyio', 'Atung')
# my_function('Gwazi')
# my_function('Chaayan')
# my_function('Yashim')

# Without inputing the lastname, we will encounter tyoeError stating missing last_name
#So to resolve the problem, we must input the last names for all persons example
# def my_function(first_name, last_name):
#     print(first_name + ' ' + last_name)
# 
# my_function('Ninyio', 'Atung')
# my_function('Gwazi', 'Atung')
# my_function('Chaayan', 'Atung')
# my_function('Yashim', 'Atung')

#Arbitrary argument
# def children(*kids):
#     print('The eldest child', kids[2])
# children('James', 'Ninyio', 'Swanyin', 'Gwazi')

# Keyword argument
# def children(kid1, kid2, kid3, kid4):
#     print('The youngest child is ' + kid1)
# children('James', 'Ninyio', 'Swanyin', 'Gwazi')
# 
# children(kid1= 'James', kid2= 'Ninyio', kid3= 'Swanyin', kid4= 'Gwazi')

# Default parameter

# def my_city(country ='Nigeria'):
#     print('I am from ' + country)
# my_city('Abuja')
# my_city('Asaba')
# my_city('Kaduna')
# my_city('Texas')

# list come back to this
def my_food(food):
    for y is food:
        print(y)       
fruits = ['apple', 'orange', 'banana']

# #my_food(fruits)


#  using return
def my_data(y):
    return 10 * y

print (my_data(2))
print (my_data(5))
print (my_data(4))
