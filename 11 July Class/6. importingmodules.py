# import modulesimport
# 
# modulesimport.welcome('Sandra')

#built-in time
# import modulesimport as dt
# dt.welcome('Sandra')


# import datetime
# my_time = datetime.datetime.now()
# print(my_time)
# print(my_time.year)
# print(my_time.strftime("%A"))
# 
# import datetime
# my_time = datetime.datetime(2023, 9, 21)
# print(my_time)


import datetime
my_time = datetime.datetime(2023, 9, 21)
print(my_time.strftime("%d"))
print(my_time.strftime("%b"))
print(my_time.strftime("%B"))
print(my_time.strftime("%m"))
print(my_time.strftime("%y"))
print(my_time.strftime("%Y"))
print(my_time.strftime("%p"))
print(my_time.strftime("%S"))

#check for daytime format codes