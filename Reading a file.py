file = open("eidNatok2020.txt","r+")
#print(file.readable())
"""text = file.read()
print(text)

size = len(text)
print(size)"""

"""text = file.readline()
print(text)
text = file.readlines()[1]
print(text)
text = file.readlines()
print(text)
"""

for line in file:
    print(line)

file.close()