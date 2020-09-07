books=[]
books.append("c")
books.append("c++")
books.append("java")
books.append("swift")
books.append("python")
print(books)

books.pop()
print("The new top book is :",books[-1])
books.pop()
print("The new top book is :",books[-1])
books.pop()
print("The new top book is :",books[-1])
books.pop()
print("The new top book is :",books[-1])
books.pop()
if not books:
    print("Not books left")