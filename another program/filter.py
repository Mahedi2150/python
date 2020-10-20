num=[1,1,2,3,3,5,6,7,7,4,3,9,5,6,7,8,4,2,6]

result =list(filter((lambda n:n%2==0),num))
print("Even Number :",result)