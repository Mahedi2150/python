import functools
def addTwoValue(num1,num2):
    return num1+num2

list1 = [12,4,5,8]

result = functools.reduce(addTwoValue,list1)
print(result)