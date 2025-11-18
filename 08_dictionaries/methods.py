# dict operations
dict_nums = {1:10,2:20,3:30}
print(dir(dict_nums))

# update() - adds / update dict items
fruits = {"a":"apple","b":"banana"}
print(fruits)
fruits.update({"c":"cherry"})
print(fruits)
 
# pop() - removes item with specific key
fruits = {"a":"apple","b":"banana"}
print(fruits)
fruits.pop("b")
print(fruits)

# popitem() - removes last item
fruits = {"a":"apple","b":"banana"}
print(fruits)
fruits.update({"c":"cherry"})
print(fruits)
fruits.popitem()
print(fruits)

# clear() - remove all items
fruits = {"a":"apple","b":"banana"}
print(fruits)
fruits.clear()
print(fruits)

# get() - get the value for key
dict_nums = {1:10,2:20,3:30}
print(dict_nums)
print(dict_nums[3])

print(dict_nums.get(0))

# keys() - return all the keys only
dict_nums = {1:10,2:20,3:30}
print(dict_nums.keys())

dict_nums = {1:10,2:20,3:30}
only_keys = dict_nums.keys()
for i in only_keys:
    print(i)

# values() - return all the values only
dict_nums = {1:10,2:20,3:30}
print(dict_nums.values())

dict_nums = {1:10,2:20,3:30}
only_values = dict_nums.values()
for i in only_values:
    print(i)

# items() - return both keys and values
dict_nums = {1:10,2:20,3:30}
print(dict_nums.items())

#copy() - creates shallow copry
dict_nums = {1:10,2:20,3:30}
bk_dict_nums = dict_nums.copy()

print(dict_nums)
print(bk_dict_nums)

bk_dict_nums.update({4:40})

print(dict_nums)
print(bk_dict_nums)

# soft copy using assignment
dict_nums = {1:10,2:20,3:30}
bk_dict_nums = dict_nums

bk_dict_nums.update({4:40})

print(dict_nums)
print(bk_dict_nums)

# setdefault() - returns valu of a key, if not present sets it
# if the key is present it will not update
dict_nums = {1:10,2:20,3:30}
print(dict_nums)

dict_nums.setdefault(3,40)
print(dict_nums)

dict_nums = {1:10,2:20,3:30,1:100,4:100}
print(dict_nums)