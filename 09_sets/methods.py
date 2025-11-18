# methods
# add() - add an element
s1 = {10,20,30,40,50}
s1.add(60)
s1.add(70)
print(s1)

# update() - add multiple elements from iterables only
s1 = {10,20,30,40,50}
s1.update([60,70])
print(s1)
s1.update((80,90,100),[10,20,40])
print(s1)

# remove() - remove a specific element, raises error if not found
s1 = {10,20,30,40,50}
s1.remove(10)
print(s1)

# discard() - remove a specific element, raises no error if not found
s1 = {10,20,30,40,50}
s1.discard(60)
print(s1)
s1.discard(10)
print(s1)

# clear() - removes all elements
s1 = {10,20,30,40,50}
s1.clear()
print(s1)

# pop() - remove an random/ arbitrary element
s1 = {10,20,30,40,50}
s1.pop()
print(s1)


#set specific operations
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

# union() - combines elements from both sets
print(s1.union(s2))
print(s1 | s2)

# intersection_update() - extract only common elements
print(s1)
print(s2)
print(s1.intersection(s2))
print(s1 & s2)
print(s1)
print(s2)

# intersection_update() - extract only common elements, updates the calling set
print(s1)
print(s2)
print(s1.intersection_update(s2))
print(s1)
print(s2)

# difference() - removes the elements which also occur in the order set
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1)
print(s2)
print(s1.difference(s2))
print(s1-s2)
print(s1)
print(s2)

# difference_update() - removes the elements which also occur in the order set, updates the calling set
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1)
print(s2)
print(s1.difference_update(s2))
print(s1)
print(s2)

# symmetric difference() - removes common elements and take combine elements left in both sets
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1)
print(s2)
print(s1.symmetric_difference(s2))
print(s1^s2)
print(s1)
print(s2)

# symmetric difference_update() - removes common elements and take combine elements left in both sets, updates the calling set
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1)
print(s2)
print(s1.symmetric_difference_update(s2))
print(s1)
print(s2)

#issubset() - checks if the given set subset of another set
s1 = {10,20,30,40,50}
s2 = {40,50}
print(s2.issubset(s1))

#issuperset() - checks if the given set supersubset of another set
s1 = {10,20,30,40,50}
s2 = {40,50}
print(s1.issuperset(s2))
print(s2.issuperset(s1))

#isdisjoint() - checks if two sets have no common elements
s1 = {10,20,30,40,50}
s2 = {40,50}
s3 = {60,70,80}
print(s1.isdisjoint(s2))
print(s2.isdisjoint(s1))

# copy() - creates a shallow copy
s1 = {10,20,30,40,50}
s2 = s1
print(s1)
print(s2)

s2.add(60)
print(s1)
print(s2)

s1 = {10,20,30,40,50}

# frozen set creates a class
fs = frozenset({10,20,30,40,50})
print(type(fs))
print(fs)
print(dir(fs))

# frozen set operations
fs1 = frozenset({10,20,30,40,50})
fs2 = frozenset({40,50,60,70,80})

print(fs1.union(fs2))