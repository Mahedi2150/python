list = [1,["mahedi",2150,5.6,[3.05,3.43,3.23,3.05]],5,6,7,3,9,3]
print(list)

#chage list item
list[0]=5
print(list)

#print index value
print(list[1])
print(list[1][0])
print(list[1][3][2])


#list extend
list = list+[100,100,200,300]
print(list)
list.extend([50200,90200,70200])
print(list)
list.remove(50200)
print(list)
print(list.count(3))

#remove index
list.remove(list[1])
print(list)

