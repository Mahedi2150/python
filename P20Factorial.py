
"""
n = int(input("Enter a number :"))
f =1
for i in range(1,n+1):
    f = f * i
print(f)
"""
#-----------------------------
"""

def fact(x):
    f = 1
    for i in range(1,x+1):
        f = f * i
    return f
result = fact(5)
print(result)
"""

#--------------------------


"""
import mat
fact = math.factorial(5)
print(fact)
"""

def fact(n):
   if(n==1):
        return 1
   else:
        return n * fact(n-1)
f = fact(5)
print(f)

