# dictionaries
empty_dict = {}
print(type(empty_dict))
print(empty_dict)

# list - [10,20,30]
# tuple - (10,20,30)
# dictionaries - (key:value)

# numbers dict
dict_nums = {1:10,2:20,3:30}
print(dict_nums)
print(dict_nums[3])

# text dict
dict_text =  {"course1":"python","course2":"java","course3":"c","course4":"sql"}
print(dict_text)
print(dict_text["course1"])

# mixed dict
dict_mixed = {1:10,"course1":"python"}
print(dict_mixed)
print(dict_mixed["course1"])

# dict inside dict
students ={
    "101":{
        "name":"avi",
        "email":"avi1@gmail.com",
        "course":"python"
    },
    "102":{
        "name":"ravi",
        "email":"ravi1@gmail.com",
        "course":"java"
    },
    "101":{
        "name":"pavan",
        "email":"pavan1@gmail.com",
        "course":"c"
    }
}
print(students)

#
nums = {(1,2,3):"python"}
print(nums)

#
dict_sub_dict = {101:["ravi","python","9am"],102:("avi","java","10am")}
print(dict_sub_dict)

# update data - methods
fruits = {"a":"apple","b":"banana"}
print(fruits)

# use assignment to add new item
fruits["c"] = "cherry"
print(fruits)

#use assignment to update exsisting item
fruits["a"] = "apricot"
print(fruits)

#class dict same as list and tuples
empty_dict = dict()
print(type(empty_dict))
print(empty_dict)

# list - [10,20,30]
# tuple - (10,20,30)
# dictionaries - (key:value)

# numbers dict
dict_nums = dict({1:10,2:20,3:30})
print(dict_nums)
print(dict_nums[3])
