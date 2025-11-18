# polymorphism
class Dog:
    def speak(self):
        print("dog woof")
    
class Cat:
    def speak(self):
        print("cat meow")
    
dog = Dog()
cat = Cat()

dog.speak()
cat.speak()

# pre defined - use cases for polymorphism
print(len("hello"))
print(len([1, 2, 3]))
print(len({1:"a",2:"b"}))

# based on operators (operator overloading)
print(2 + 3)
print("hello" + "world")
print([1, 2] + [3, 4])

# common use case functionality
class Circle:
    def area(self):
        return 3.14 *5*5
    
class Square:
    def area(self):
        return 5*5
    
def print_area(shape):
    print("area: ", shape.area())

print(print_area(Circle()))
print(print_area(Square()))

# real world use case - database connection
class MySQL:
    def connect(self):
        return "MySQL database connected"   
    
class PostgreSQL:
    def connect(self):
        return "PostgreSQL database connected"
    
def open_connection(db):
    print(db.connect())

open_connection(MySQL())
open_connection(PostgreSQL())

#method overloading - not accepted in python
class Math:
    def add(self, a, b):
        return a + b
    def add(self, a, b):
        return a + b
    
add_obj = Math()
print(add_obj.add(2, 3))    
# print(add_obj.add(2, 3, 4))  # this will give error

# duck typing - if it walks like a duck and quacks like a duck, then it is a duck
class Duck:
    def quack(self):
        print("duck quacks")

class Person:
    def quack(self):
        print("person quacks like a duck")

def make_it_quack(obj):
    obj.quack() 

make_it_quack(Duck())
make_it_quack(Person())