class phone:
    def call(self):
        print("You can call")
    def message(self):
        print("You can message")

class samsung(phone):
    def photo(self):
        print("You can take photo")
        
print(issubclass(samsung,phone))
p=phone()
p.call()
p.message()

s=samsung()
s.call()
s.message()
s.photo()

