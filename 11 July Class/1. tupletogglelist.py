# #toggle: this used parenthesis unlike list which uses square brackets. It has a defined order which can't be
# #changed, it allows the duplicate of an item. Same as tuple ish.
# items = ('pen', 'book', 'desk', 'book')
# print(items)
# print(len(items))


# #tuple: for it to be a tuple it must come with the comma
# item1 = ('books',)
# print(type(item1))


# # tuple can be of any datatype; boolean, string, int etc. They are unchangeable. They are like list.
# #NOTE: you can access a particular item by using its index number
# item1 = ('books', 76, True, 'pen', False, 87)
# print(item1[-1])
# print(item1[2:4])


# item1 = ('books', 76, True, 'pen', False, 87)
# if 'pencil' in item1:
#     print('pen exixts')
# else:
#     print('does not exist')
    

#To change a tuple, you have to change it to a list and then change it back to a tuple.
item1 = ('books', 76, True, 'pen', False, 87)
fruits = ('apple', 'kiwi', 'pawpaw', 'orange')
x = list(fruits)
x[1] = 'mango'
print(x)
fruits = tuple(x)
print(fruits)

#To make any changes, you'll have to change it back to a list e.g. to insert anything etc.