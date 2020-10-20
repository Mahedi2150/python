name = ['Mahedi','Numan','karim','Mizan','Anis']
age = [20,23,21,22,24]
combineTwoList = list(zip("12345",name,age))

print(combineTwoList)


print("\nUnzip program ..>\n")


all_info = [('1', 'Mahedi', 20), ('2', 'Numan', 23), ('3', 'karim', 21), ('4', 'Mizan', 22), ('5', 'Anis', 24)]

unzip_all=list(zip(*all_info))
print(unzip_all)

serial = unzip_all[0]
print(serial)

unzip_name = unzip_all[1]
print(unzip_name)

unzip_age = unzip_all[2]
print(unzip_age)