# i have a file on persistent storage

# we have open function

# 1st syntax
# open("filepath",mode)
    # mode - rwa

file = open("file.txt","r")
# print(type(file))
print(file)
print(file.closed)
file.close()
print(file.closed)


# 2st syntax
# with open("filepath",mode)
    # mode - rwa

# read mode
with open("file.txt","r") as file_new:
    # print(type(file_new))
    print(file_new)
    # print(file_new.read())
    
    # for character in file_new.read():  # character by character
        # print(character)

    # print(file_new.readline())
    # print(file_new.readline())
    for line in file_new.readlines():
        print(line.strip())

# print(file_new.closed)

# write mode
# create file
with open("new.txt","w") as file_new:
    #print(file_new)
    file_new.write("welcome to java \n")
    file_new.write("welcome to python \n")
    file_new.write("welcome to git ")

with open("data.txt","w") as file_new:
    #print(file_new)
    file_new.writelines(["welcome to java \n","welcome to python \n","welcome to git"])

# append mode
with open("data.txt","a") as file_new:
    #print(file_new)
    file_new.writelines(["welcome to cloud \n","welcome to devops \n","welcome to ds"])


# delete a file
# os module
import os
os.remove("data.txt")

# working with csv files
# read data
import csv
with open("sample_data.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    print(csv_reader)
    for row in csv_reader:
        # print(row)

# get the coustomers from hyd
        #if row[3] == "hyd":
        #   print(row)

# get the coustomers from gmail
        if row[1].endswith("@gmail.com"):
            print(row)

# DictReader -- gives the dictionary object
with open("sample_data.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    print(csv_reader)
    for row in csv_reader:
        if row["email"].endswith("@gmail.com"):
             print(row)

# now writing the data
with open("write_data.csv","w") as file_data:
    csv_writer = csv.writer(file_data)
    csv_writer.writerow(['name','email','mobile','location'])
    csv_writer.writerow(['avi','avi@gmail.com','989898','hyd'])
    csv_writer.writerows([['avi','avi@gmail.com','989898','hyd'],['ravi','ravi@gmail.com','878787','pune']])

# now append the data
with open("write_data.csv","a") as file_data:
    csv_writer = csv.writer(file_data)
    csv_writer.writerows([['user1','user1@gmail.com','989898','hyd'],['user2','user2@gmail.com','878787','pune']])

# working with json data
import json
student = {
    "id": 101,
    "name": "avi",
    "course": "python full stack",
    "skills": ["python","java"],
    "score": 92.3
}

print(type(student))

# now writing the data
with open("student.json","w") as file_data:
    json.dump(student,file_data,indent=5)

# now read the data
with open("student.json","r") as file_data:
    json_data = json.load(file_data)
    print(json_data)
    print(type(json_data))
    print(json_data['name'])
    print(json_data['skills'][0])

# ops b/w json & py data
# convert python json data to string data
student_json = json.dumps(student)
print(student_json)

# convert string data to json
json_string = '{"id": 102,"name": "avi","corse": "aiml"}'
print(type(json_string))
stu_data = json.loads(json_string)
print(stu_data)
print(type(stu_data))