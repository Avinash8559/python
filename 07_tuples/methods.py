# 1 index() return the index position of element
tuples_nums = [10,20,30,40,50]
print(tuples_nums.index(30))

# 2 count() counts and returns number of times a element present
tuples_nums = [10,20,30,40,50,10]
print(tuples_nums.count(10))

# tuples packing and unpacking
person = ("john",25,"python")  # packing
name,age,course = person  # unpacking

print(name)
print(age)
print(course)

t1 = ([10,20],[30,40],[50,60])
print(t1[0][0])

t1 = ([10,20],[30,40],[50,60])
print(t1)
t1[0][0] = 100
print(t1)