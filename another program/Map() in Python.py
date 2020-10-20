"""def mulFiveTimes(number):
    return number*5
result = []
num = [3,5,7,9,1,5]

for i in num:
    result.append(mulFiveTimes(i))

print(result)"""


def mulFiveTimes(number):
    return number*5
num = [3,5,7,9,1,5]

print(list(map(mulFiveTimes,num)))