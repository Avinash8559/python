# without functions
a = 10
b = 12
print(a+b)
print(a-b)
print(a*b)
print(a/b)

a = 18
b = 20
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("="*50)

a = 100
b = 200
# define a function
def arithmetic():
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

# call a function - 100,200
arithmetic()

a = 1000
b = 2000

# call a function - 1000,2000
arithmetic()

print("="*50)

# functions with parameters
def arithmetic(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

# call a function
arithmetic(5000,1000)
arithmetic(100,500)

print("="*50)


# functions without return keyword
def add(a,b):
    a+b
print(add(10,20))

# function with return keyword
def add(a,b):
    return a+b
print(add(10,20))

# function with return , give appropriate responses
def add(a,b):
    return "hello there"
print(add(10,20))


def new_math(a,b):
    return a+b
    return a-b
    return a*b

print(new_math(100,200))


def math_new(a,b,opr):
    if opr == "+":
        return a+b
    elif opr == "-":
        return a-b
    elif opr == "*":
        return a*b
    elif opr == "/":
        return a/b
    else:
        return "invalid operator"
    print("code is unreachable ")
    
print(math_new(3,4,"+"))
print(math_new(3,4,"-"))
print(math_new(3,4,"*"))
print(math_new(3,4,"/"))
print(math_new(3,4,"'")) 



# local scope for variables
def add():
    # local variables are b , c
    bb = 5
    cc = 6
    print(bb)    # accessing inside
    print(cc)    # accessing inside

add()
        # print(bb) accessing outside

# parameters passed to functions are also local variables

def add(bb,cc):    # local variablesare bb , cc
    print(bb)
    print(cc)
add(10,20)
        # print(bb) accessing outside

# global variables
aa = 30
def add(bb,cc):
    print(bb)     # inside
    print(cc)     # inside
    print(aa)     # outside
add(1,2)
print(aa)

# global variables
aa = 30
def add(bb,cc,aa):
    print(bb)     # local
    print(cc)     # local
    print(aa)     # local
    print(globals()['aa'])
add(1,2,3)
print(aa)

# trying to change global variable
count = 0
def increment():
    global count
    count += 1
increment()
print("count: ",count)

# function composition
def add(a,b):
    return a+b
print(add(1,2))

def sub(c,d,e):
    return add(c,d)-e
print(sub(3,4,5))

# to check builtins in python use _builtins_
    # print(dir(__builtins__))

# built in
text = "python"
len_text =len(text)
print("built in",len_text)

# without lambda
def add(a,b):
    return a+b
print(add(3,4))

# with lambda    lambda arguments: expressions
sum = lambda a,b: a+b
print(sum)
print(sum(5,10))

# IILE
print((lambda a,b: a+b) (100,200))
print((lambda a,b: a*b) (100,200))

# withut map
     # input [1,2,3,4]   -  output [1,4,9,16]
def square_list(numbers):
    squared_list = []
    for n in numbers:
        squared_list.append(n * n)
    return squared_list

print(square_list([1,2,3,4]))

# with map
    # input [1,2,3,4] - output [1,4,9,16]
    # one liner function
    # map(function, iterable)
print(list(map(lambda n: n * n,[1,2,3,4])))

# without filter
    # input [1,2,3,4,5,6,7,8,9,10] - output  [2,4,6,8,10]
def even_list(numbers):
    even_nums = []
    for n in numbers:
        if n % 2 == 0:
            even_nums.appemd(n)
    return

# without reduce
# input [1,2,3,4]   -- output [1*2*3*4 = 24]
def multiply_list(numbers):
    result = 1
    for i in numbers:
        result = result * 1
    return result

print(multiply_list([1,2,3,4]))

# with reduce
from functools import reduce
print(reduce(lambda x,y: x*y,[1,2,3,4]))