# empty set
empty_set = {}
print(type(empty_set))
print(empty_set)

# use set class
empty_set = set()
print(type(empty_set))
print(empty_set)

print(dir(empty_set))

# numbers set
set_nums = {10,20,30,40,50}
print(set_nums)

# duplicaes eliminated
set_nums = {10,20,30,40,50,40,50,20,10}
print(set_nums)

# index will not work
set_nums = {10,20,30,40,50}
# print(set_nums[2])

# text data
set_text =  {"python","java","c","sql"}
print(set_text)

# mixed dict
set_mixed = {"python","java","c","sql",10,20,30,40,50}
print(set_mixed)

# accessing data in sets
set_nums = {10,20,30,40,50}
for i in set_nums:
    print(i)

list_nums = list(set_nums)
print(list_nums)
print(list_nums[1])