a = 5

try:
    print("Resource Open")
    n = int(input("Enter any number :"))
    print(a/n)
except ZeroDivisionError:
    print("You can not divide a number by Zero!")
except ValueError:
    print("Something Wrong!")
finally:
    print("Resource Close:")

print("Ok bye !!")