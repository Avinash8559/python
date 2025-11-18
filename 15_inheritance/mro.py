# mro - method resolution order
class A:
    def show(self):
        print("a show")

class B:
    def show(self):
        print("b show")

class C(A,B):
    pass

obj = C()
obj.show()
print(C.mro)

# super()
class Parent:
    def great(self):
        print("hello from parent")

class Child(Parent):
    def great(self):
        super().great()
        print("hello from child")

child = Child()
child.great()