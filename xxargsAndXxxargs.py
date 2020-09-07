#xxargs

"""def student(*details):
    print(details[1])

student(101,'mahedi')
student(102,'hasan',3.50)"""

def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)

add(20,30)
add(20,30,40)
add(20,30,40,50)

#xxxargs
def student(**details):
    print(details["name"])

student(id=101,name="Mahedi")