# position arguments
def login(username,password):
    if username == "avi" and password == "12345":
        print('login success')
    else:
        print("login faild")

login("avi","12345")
login("avi","123")
login("12345","avi")

# default arguments
def emp_info(emp_name,emp_email,emp_loc = "hyd",emp_add = "india"):
    print(f"hi {emp_name} your email is {emp_email} and location is {emp_loc} actually from {emp_add}")

emp_info("avi","avi@gmail.com","hyd")
emp_info("ravi","ravi@gamil.com")
emp_info("pavan","pavan@gamil.com","banglore")
emp_info("ajay","ajay@gamil.com","banglore","pune")

# keyword arguments
def emp_info(emp_name,emp_email,emp_loc,emp_add = "india"):
    print(f"hi {emp_name} your email is {emp_email} and location is {emp_loc} actually from {emp_add}")

emp_info(emp_name = "avi",emp_loc = "hyd",emp_email = "avi@gmail.com")

# arbitrary positional arguments
def add_all(*numbers):
    total = 0
    for i in numbers:
        total = total + 1
    print(f"total is: {total}")

add_all(1)
add_all(1,2,3)
add_all(1,2,3,4,5,6,7,8,9)

# arbitrary keyword arguments
def profile(**info):
    print(info)

profile()
profile(id = 101)
profile(id = 102,name = "avi")

# transactions
def cred_trans(**trans):
    print(trans)
    total = 0
    for i in trans:
        total = total+trans[i]
        print(f"you have done {len(trans)} and total value of all transactionns is {total}")

cred_trans(jan=1000, feb=2000, mar=3000)

# using both *args and **kwargs
def cred_trans_new(*trans,**info):
    print(trans)
    print(info)
    total = 0
    for i in trans:
        total = total + i
    print(f"hi {info['name']} you have done {total} amount of transactions")

cred_trans_new(1000,3000,5000,name="avi",email="avi@gmail.com")