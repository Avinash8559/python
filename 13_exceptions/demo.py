# exeption handling
# when there are no errors nothing to handle
print("program execution started")
num1 = 10
num2 = 5
print(num1/num2)
print("program execution completed")
print("="*50)

# when there are errors, see how python handles them
print("program execution started")
num1 = 10
num2 = 0 

try:
    print(num1/num2)
except:
    print("oops! you cant divide by zero")
print("program execution completed")
print("="*50)

# when there are errors, see how youcan handles multiple errors
print("program execution started")
data = [1,2,'python',0,4]
for i in data:
    try:
        print(1/i)
    except TypeError:
        # print(sys.exp_info())
        print("oops! dont pass strings")
    except ZeroDivisionError:
        print("oops! you cant divide by zero")
print("program execution completed")
print("="*50)
 
# ===============
print("program execution started")
num1 = 10
num2 = 5

try:
    print(num1/num2)
except:
    print("oops! you cant divide by zero")
else:
    print("calculation successfull")
finally:
    print("program execution completed")
print("="*50)

# exception class
# print(help(Exception))

# based on my req -- we need a coustom exception


class InvalidScoreError(Exception):
    pass

try:
    score = int(input("enter score (0-100):  "))
    if score < 0 or score > 100:
        raise InvalidScoreError("score must be between (0-100)")
    print("your score is valid")
except InvalidScoreError as e:
    print("error",e)



class AgeTooYoungError(Exception):
    pass
 
class NoIdError(Exception):
    pass
try:
    age = int(input("enter age:  "))
    if age < 18:
        raise AgeTooYoungError
    has_id = input("do you have id ? (yes/no)")
    if has_id != "yes":
        raise NoIdError
except AgeTooYoungError:
    print("you must be 18 years old to register")

except NoIdError:
    print("you must have an id to register")
else:
    print("registration successful")