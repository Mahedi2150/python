num = [20,30,40,50,60,70,80,90]
print(num)

"""
n = len(num)
index = 0
while index < n:
    print(num[index])
    index=index+1
"""
sum = 0
for x in num:
    sum = sum +x
    print(x)
print("Sum of list :",sum)