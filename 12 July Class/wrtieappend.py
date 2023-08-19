# w overwrites(replaces) everything
# f = open("untitled.py", "w")
# f.write("Here we go!!")
# f.close()


f = open("modulesimport.py", "a")
f.write("\nHere we go!!")
f.close()


f = open("modulesimport.py", "r")
print(f.read())