# impleentation of loops

# while loop
count =1
while count <=5:
    print(count)
    count+=1

# best use case to understand while
password ="python123"
user_input=""

while user_input != password:
    user_input = input("enter password ")
print("access granted")

#for loop
#for element in sequence

text = "python"
for i in text:
    print(i)

# we cant use for to iterate non iterable objects
#num = 10
#for i in num:
#    print(i)

#we can use for to  iterate iterable objects
list = [10]
print(dir(list))
for i in list:
    print(i)

# automated hi 10 times
for i in range(10):
    print("Hi")

for i in range(3,10):
    print("Hello")

for i in range(1,10,2):
    print(i)

# even numbers 1-20
# one approach
i=2
while i <= 20:
    print(i)
    i+=2

# second approach
i=2
while i <= 20:
    if i%2==0:
        print(i)
    i+=1

# for loop even 1-20
i=2
for i in range(2,21,2):
    print(i)


#nested for loop
for i in range(1,4):
    for j in range(1,11):
        print(f"{i} x {j}  ={i*j}")

#nested while loop
i = 1
while i < 4:
    j = 1
    while j <= 10:
        print(f"{i} x {j}  ={i*j}")
        j += 1
    i += 1 

#break
for i in range(5):
    if i==3:
        break
    print(i)

#continue
for i in range(5):
    if i==3:
        continue
    print(i)

#pass
if (5>9):
    pass
