#Task 1: __str__ and __repr__ 
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"Book: {self.title} by {self.author}, Price: {self.price}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.price})"


b1 = Book("Python Basics", "Ravi", 300)
b2 = Book("OOP Concepts", "Anita", 450)

print(b1)
print([b1, b2])


#Task 2: __eq__ (Equality Checking Task)

class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __eq__(self, other):
        return self.brand == other.brand and self.model == other.model
m1 = Mobile("Samsung", "S21", 50000)
m2 = Mobile("Samsung", "S21", 52000)
m3 = Mobile("Apple", "iPhone13", 70000)

print(m1 == m2)
print(m1 == m3)


#Task 3: __new__ and __init__ (Object Creation Flow Task)

class User:
    def __new__(cls, *args):
        print("Object is being created")

    def __init__(self, name):
        print("Object is initialized")
        self.name = name
u = User("Poorvi")



#Task 4: __enter__ and __exit__ (Context Manager Task)

class DatabaseConnection:
    def __enter__(self):
        print("Database Connected")
        
    def __exit__(self, Data_connect, Data_query, Data_exit):
        print("Database Closed")


with DatabaseConnection():
    print("Performing Query...")
    
    

#Task 5: __call__ (Callable Object Task)

class Calculator:
    def __call__(self, a, b):
        return a + b


obj = Calculator()
print(obj(10, 20))



#Task 6: __getitem__ and __setitem__ (Indexing Task)

class ShoppingCart:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value


cart = ShoppingCart(["Apple", "Banana", "Milk"])

print(cart[0])

cart[1] = "Orange"
print(cart.items)


#Task 7: __del__ (Destructor Task)

class Session:
    def __del__(self):
        print("Session Ended")


obj = Session()
del obj


#Task 8: __contains__ (Membership Operator Task)

class Library:
    def __init__(self, books):
        self.books = books

    def __contains__(self, item):
        return item in self.books


library = Library(["Python", "Java", "C++"])

print("Python" in library)



#Task 9: __gt__, __lt__ (Comparison Task)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __lt__(self, other):
        return self.salary < other.salary


e1 = Employee("Amit", 50000)
e2 = Employee("Ravi", 60000)

print(e1 > e2)
print(e1 < e2)



#Task 10: __iter__ and __next__ (Custom Iterator Task)

class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration


for i in Counter(1, 5):
    print(i)