d1 = {
    "name":"Mahedi",
    "age":22,
    "ht":5.6
}
print(d1.get("ht","not found"))

x = len(d1)
print(x)

d1["varsity"]="Daffodil International University"
print(d1)

x = len(d1)
print(x)


d2 = d1.copy()
print(d2)

print(d2.keys())
print(d2.values())
print(d2.items())