s1 = {1,2,3,4,1,2,3,4}
s2 = {9,10}
s1.update([5,6,7,8],s2)
print(s1)
s1.remove(1)
print(s1)

#s1.remove(15)
s1.discard(15)
print(s1)