subject = ['c','c++','java','python','ruby','android']
print(subject)
pos = subject.index('c++')
print(pos)
print(subject[3])
print(subject[:2])
print(subject[2:])
print(subject[-2])
print("python" in subject)
print("swift" in subject)
print(subject+['R'])

#paet-2

lenth =len(subject)
print(lenth)

subject.append('sql')
print(subject)
print(subject[2:])

subject.insert(2,'os')
print(subject)

subject.remove('ruby')
print(subject)

subject.sort()
print(subject)

subject.reverse()
print(subject)

subject.pop()
print(subject)

subject.pop()
print(subject)




sub2= subject.copy()
print(sub2)
sub2.clear()
print(sub2)


country =['bangladesh']*3
#country2 =country*3
#print(country2)
x =country.count('bangladesh')
print(x)