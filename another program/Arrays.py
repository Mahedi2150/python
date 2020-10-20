from array import *

#i = int  f = float

salary = array("i",[1856,1633,1252,1546,8541])
for i in range(len(salary)):
    print(salary[i])
print("---------")

salary1 = array("f",[2000.5,500.5,1000.5,6000.5])

for i in range(len(salary1)):
    print(salary1[i])

print(salary1.append(99999))
print(salary1)
print(salary1.remove(500.5))
print(salary1)
print(salary1.reverse())
print(salary1)
