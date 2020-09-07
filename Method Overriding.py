class phone:
    def __init__(self):
        print("I am in phone calss")

class samsung(phone):
    #init
    def __init__(self):
        super(samsung, self).__init__()
        print("I am in samsung class")
s=samsung()

