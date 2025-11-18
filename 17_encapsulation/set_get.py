# without setter and getter
class Student:
    def __init__(self, age):
        self.__age = age

s = Student(20)
print(s._Student__age)   # accessing directly

s._Student__age = -5     # no validation
print(s._Student__age)


# with setter and getter
class Student:
    def __init__(self, age):
        self.__age = age

    # setter
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")

    # getter
    def get_age(self):
        return self.__age
    
s = Student(15)
print(s.get_age())        # accessing through getter

s.set_age(20)             # accessing through setter
print(s.get_age())        # accessing through getter



# @property decorator - python way of setter and getter
class Student:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):       # getter
        return self.__age

    @age.setter
    def age(self, age):   # setter
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")

s = Student(25)
print(s.age)             # accessing through getter

s.age = 20            # accessing through setter
print(s.age)            # accessing through getter

s.age = -5            # accessing through setter
print(s.age)            # accessing through getter