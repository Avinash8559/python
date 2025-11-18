# tuples
empty_tuple = ()
print(type(empty_tuple))
print(empty_tuple)

# numbers
tuple_nums = (10,20,30,40,50)
print(tuple_nums)

# text
tuple_courses = ("python","java","c++")
print(tuple_courses)

# mixed
tuple_mixed = ("python","java","c++",10,20,30,40,50,5.5)
print(tuple_mixed)

# tuples
empty_tuple = tuple()
print(type(empty_tuple))
print(empty_tuple)

# numbers
tuple_nums = tuple((10,20,30,40,50))
print(tuple_nums)

# text
tuple_courses = tuple(("python","java","c++"))
print(tuple_courses)

# mixed
tuple_mixed = tuple(("python","java","c++",10,20,30,40,50,5.5))
print(tuple_mixed)

tuple_int =tuple((10,))
print(tuple_int)

list_nums = [10,20,30,40,50]
print(list_nums)
tuple_nums = list_nums
print(tuple_nums)

tuple_nums = tuple(list_nums)
print(tuple_nums)

list_nums = list(tuple_nums)
print(list_nums)

# accessing the data in list
tuple_nums = [10,20,30,40,50]
first_tuple_nums = tuple_nums[0]
last_tuple_nums = tuple_nums[-1]

# indexing
print(first_tuple_nums)
print(last_tuple_nums)

#slicing
tuple_nums = (10,20,30,40,50)
print(tuple_nums[:])
print(tuple_nums[1:4:1])
print(tuple_nums[1:4:-1])
print(tuple_nums[::-1])

# looping
tuple_nums = [10,20,30,40,50]
for i in tuple_nums:
    print(i)

# using range
custom_tuple = tuple(range(0,26,5))
print(custom_tuple*2)

# loop
custom_list = tuple(range(0,26,5))
for i in custom_list:
    print(i*2)

# perform some conditions
days = ("sun","mon","tue","wed","thu","fri","sat")
day = input("enter day name in a week: ")
if day in days:
    print("day exists")
else:
    print("invalid day in week")

#tuple operations
tuple_nums = (10,20,30,40,50)
print(dir(tuple_nums))