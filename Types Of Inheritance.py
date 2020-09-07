"""#Multi Level Inheritance
class A:
    def display1(self):
        print("I am inside A class")

class B(A):
    def display2(self):
        print("I am inside B class")

class C(B):
    def display3(self):
        super(C, self).display1()
        super(C, self).display2()
        print("I am inside C class")

obj = C()
obj.display3()"""

#Multiple Inheritance
class A:
    def display(self):
        print("I am inside A class")

class B:
    def display(self):
        print("I am inside B class")

class C(B,A):
       pass

obj = C()
obj.display()

