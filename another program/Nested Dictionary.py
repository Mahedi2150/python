studentId = {1 : {"name" : "Mahedi","age":22,"section":"PC-B"},
             2 : {"name" : "shohag","age":22.5,"section":"PC-A"},
             3 : {"name" : "XYZ","age":23,"section":"PC-c"}
             }

print(studentId)
print(studentId.get(2,"Not Found"))

print(studentId[3]["name"])

studentId[4] = {}
studentId[4]["name"]= "Bijoy"
studentId[4]["age"]= 23
studentId[4]["section"]= "PC-B"

print(studentId)

del studentId[4]["age"]
print(studentId[4])



print(studentId)