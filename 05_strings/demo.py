# '' single word
# "" single lines
# """""" multi lines
question = "how are you"
answer = " i am fine "
print(answer)

answer = " i'am fine "
print(answer)

answer = ' i am "good" '
print(answer)

answer = """ i'm fire and "good" """
print(answer)

# accessing by index
text = "python"
print(text[0])
print(text[2])

# using for loop to access
for i in text:
    print(i)

# slicing
text = "python"
print(text[0:3])
print(text[1:])
print(text[:5])
print(text[:])
print(text)

print(text[1:4:1])
print(text[0:5:2])

text = "python is very easy to learn"
print(text[0:16:2])

# negative indexing
text = "python"
print(text[-4:-1])
print(text[-4:-1:1])
print(text[-4:-1:-1])

#reverse
text = "python"
print(text[::-1])

# string immutability
#text = "python"
#text[0] = "P"
#print(text)

# reassigning
text = "python"
text = "Pyhon"
print(text)

new_text = "J" + text[1:]
print(new_text)

# concat (+) join string
# repeat (*) repeat string
# concat -> join multiple strings
str = "hi "
print(str*5)

#string operations -> string methods
print(dir(str))

mobile_number = input("enter mobile number ")
valid_number = mobile_number.isdigit()
print(valid_number)

pan_number = input("enter pan number ")
valid_pan_number = pan_number.isalnum()
format_valid_pan_number = pan_number.upper()
print(format_valid_pan_number)