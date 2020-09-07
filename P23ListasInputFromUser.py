
n = input("Enter a text a number :")
list = n.split()
sum = 0
for x in list:
    sum = sum+int(x)
print(sum)

"""


numofword = 0
numofletter = 0
numofdigite = 0

n = input("Enter a text of number :")
for x in n:
    x.upper()
    if x>='a'and x<='z':
        numofletter = numofletter+1
    elif x>='0' and x<='9':
        numofdigite = numofdigite+1
    elif x==" ":
        numofword = numofword+1
print("Number of words :",numofword+1)
print("Number of letter :",numofletter)
print("Number of digits :",numofdigite)


numberofletter = 0
n = input("Enter a text :")
for x in n:
    x.upper()
    if x=="a":
        numberofletter = numberofletter+1
print(numberofletter)


"""



