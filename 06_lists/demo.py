# define a list
empty_list = []
print(type(empty_list))
print(empty_list)

# define a list with nums
list_nums = [10,20,30,40,50]
print(type(list_nums))
print(list_nums)

# duplicates
list_nums = [10,20,30,40,50,50,50,40]
print(type(list_nums))
print(list_nums)

# define a list with text
list_courses = ["python","java","c++","c","sql"]
print(type(list_courses))
print(list_courses)

# define a list with mixed
list_mixed = [10,20,30,40,50,"python","java","c++","c","sql"]
print(type(list_mixed))
print(list_mixed)

# define inside list
list_nest = [10,20,30,40,50,["python","java","c++","c","sql"]]
print(type(list_nest))
print(list_nest)

# using class list
empty_list = list()
print(type(empty_list))
print(empty_list)

list_nums = list([10,20,30,40,50])
print(type(list_nums))
print(list_nums)

list_nums = list([10])
print(type(list_nums))
print(list_nums)

# accessing the data in list
list_nums = [10,20,30,40,50]
first_list_nums = list_nums[0]
last_list_nums = list_nums[-1]

# indexing
print(first_list_nums)
print(last_list_nums)

#slicing
print(list_nums[:])
print(list_nums[1:4:1])
print(list_nums[1:4:-1])
print(list_nums[::-1])

# get to know memory management with data
list_1 = [10,20,30,40,50]
list_2 = [10,20,30,40,50]
print(id(list_1))
print(id(list_2))

num1 = 10
num2 = 10
print(id(num1))
print(id(num2))

print(id(list_1[0]))
print(id(list_2[0]))

list_nums = [10,20,30,40,50]
print(dir(list_nums))

# looping
list_nums = [10,20,30,40,50]
for i in list_nums:
    print(i)

# using range
custom_list = list(range(0,26,5))
print(custom_list*2)

# loop
custom_list = list(range(0,26,5))
for i in custom_list:
    print(i*2)

# perform some conditions
days = ["sun","mon","tue","wed","thu","fri","sat"]
day = input("enter day name in a week: ")
if day in days:
    print("day exists")
else:
    print("invalid day in week")

l1 = [(10,20),(30,40),(50,60)]
print(l1)
l1[1] = (100,200)
print(l1)