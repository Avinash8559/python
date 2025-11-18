#if
value = 10
if value>0:
    print(f"Given {value} is positive")
    print("code is executed")

#checking a number in range or not
num = 12
if num >=10 and num <=20:
    print(f"Given num {num} is in range")

#if-else
#check a num is positive or negative
num = 10
if num>0:
    print("positive")
else:
    print("negative") 

#input function
#vote eligibility using if-else
email =input("enter the mail ")
print(f"welcome: {email}")
age = int(input("enter age "))
if age>=18:
    print("can vote")
else:
    print("cant vote")

#check vote eligibility using ternory operator
age = int(input("enter age "))
status = "can vote" if age>=18 else "cant vote"
print(status)

#elif lader
score = int(input("enter score"))
if score>=90:
    print("A grade")
elif score>=75:
    print("B grade")
elif score>=50:
    print("C grade") 
elif score>=35:
    print("D grade")
else:
    print("FAIL")

#match case
choice = int(input("enter choice "))
match choice:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case 4:
        print("four")
    case _:
        print("invalid")   

#nested conditions senario
age = int(input("enter age: "))
has_id=True
if age >=21:
    if has_id:
        print("you are allowed")
    else:
        print("you need if")
else:
    print("you are too young")