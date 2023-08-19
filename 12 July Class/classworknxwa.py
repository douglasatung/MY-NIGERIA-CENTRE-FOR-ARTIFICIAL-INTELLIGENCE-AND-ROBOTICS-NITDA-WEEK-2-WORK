new_file = open("CWfile.txt", "x")
f = open("CWfile.txt", "w")
f.write("\nGood morning!!")
f.close()


f = open("CWfile.txt", "r")
print(f.read())