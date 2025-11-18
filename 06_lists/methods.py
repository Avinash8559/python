# 1 append()  it adds single element at the end of the list
list_nums = [10,20,30,40,50]
print(list_nums)

list_nums.append(60)
print(list_nums)

list_nums.append([70,80])
print(list_nums)

list_nums.append("hello")
print(list_nums)

list_nums.append("hello")
print(list_nums)

# 2 extend() can add only iterables,elements are added individuals , not as nested
list_nums = [10,20,30,40,50]
print(list_nums)

list_nums.extend([60])
print(list_nums)

list_nums.extend([70,80])
print(list_nums)

list_nums.extend("hello")
print(list_nums)

# 3 insert() based on index insert an element
list_nums = [10,30,40,50]
print(list_nums)
list_nums.insert(1,20)
print(list_nums)

list_nums.insert(len(list_nums),60)
print(list_nums)

list_nums.insert(10,100)
print(list_nums)
print(list_nums.index(100))

# 4 pop() it removes an element,by default reoves last element
list_nums = [10,20,30,40,50]
print(list_nums)
removed_element = list_nums.pop()
print(list_nums)
print(removed_element)

list_nums = [10,20,30,40,50]
print(list_nums)
removed_element = list_nums.pop(1)
print(list_nums)
print(removed_element)

# 5 remove() the matching vlaue ,not based on index
list_nums = [10,20,30,40,50,10]
list_nums.remove(10)
print(list_nums)

# 6 clear() removes all the elements 
list_nums = [10,20,30,40,50]
print(list_nums)
list_nums.clear()
print(list_nums)

# 7 index() return the index position of element
list_nums = [10,20,30,40,50]
print(list_nums.index(40))

list_nums = [10,20,30,20,40,20,10,20,10,20,10]
print(list_nums.index(20,2))
print(list_nums.index(20,4,8))

# 8 count() counts and returns number of times a element present
list_nums = [10,20,30,20,40,20,10,20,10,20,10]
print(list_nums.count(10))

# 9 reverse() reverse the elements of list, and updates original list
list_nums = [10,20,30,40,50]
print(list_nums)
list_nums.reverse()
print(list_nums)

# slicing reverses the elements of list, and dont updates original list
list_nums = [10,20,30,40,50]
print(list_nums)
print(list_nums[::-1])
print(list_nums)

# 10 sort() sorts the lists, default is ascending
list_nums = [50,20,40,10,30]
print(list_nums)
print(list_nums.sort())
print(list_nums)

list_nums = [50,20,40,10,30]
print(list_nums)
print(list_nums.sort(reverse=True))
print(list_nums)

names=["zohan","ramu","anji"]
names.sort()
print(names)

#mixed data cant be sorted

# 11 copy() creates a shallow copy, when we modify the shallow copy original copy will not affect
list_nums = [10,20,30,40,50]
print(list_nums)
bk_list_nums = list_nums.copy()
print(bk_list_nums)

bk_list_nums.append(60)
print("backup ",bk_list_nums)
print("original ",list_nums)

# soft copy use assignment operator
list_nums = [10,20,30,40,50]
print(list_nums)

bk_list_nums  = list_nums
bk_list_nums.append(60)
print("backup ",bk_list_nums)
print("original ",list_nums)