# encapsulation

# public
class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b

obj = A(10,20)

# accessing public 
print(obj.a)    
print(obj.b)



# protected
class A:
    def __init__(self,a,b):
        self.__a = a
        self.__b = b

obj = A(10,20)

# accessing protected 
print(obj._A__a)    
print(obj._A__b)



# private
class A:
    def __init__(self,a,b):
        self.__a = a
        self.__b = b

obj = A(10,20)

# accessing private
print(obj._A__a)    
print(obj._A__b)

