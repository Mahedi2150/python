num = [1,2,3,4,5]


"""result = list(map(lambda x:x*x , num))
print(result)"""


print([x*x for x in num])

"""result1 = list(filter(lambda x:x%2==0,num))
print(result1)"""

print([x for x in num if x%2==0])