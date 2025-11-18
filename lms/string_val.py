# grade tacker with strings operations

print("=" * 30)
print("enhanced lms grade tracker ")
print("=" * 30)

# validate id
student_id_valid = False
while not student_id_valid:
    student_id = input("enter your id: ")

    if student_id.startswith("-") and student_id[1:].isdigit():
        print("please input positive values only")
    elif student_id.isdigit():
        student_id = int(student_id)
        if student_id > 0:
            student_id_valid = True
        else:
            print("please input non-zero value")
    else:
        print("enter only numbers")
print(student_id)

# format id
formatted_id = "STU" + str(student_id).zfill(5)
print(formatted_id)

# validate name
student_name_valid = False
while not student_name_valid:
    student_name = input("enter student name ")
    student_name = student_name.strip().title()

    # name check should have only alphabets
    name_check = student_name.replace(" ","")
    
    #look for only alphabets
    if name_check.isalpha() and len(student_name) >= 3:
        student_name_valid = True
        print("name: "+student_name)
    else:
        if not name_check.isalpha():
            print("name should container only letters")
        elif len(student_name) < 3:
            print("name should have atleast 3 characters")

# email generation
name_part = student_name.split()
first_name = name_part[0].lower()
student_email = first_name+"." +str(student_id) + "@university.edu"
print(student_email)

# discount calculation
base_course_fee_valid = False
while not base_course_fee_valid:
    base_course_fee = input("enter your fee: ")

    if base_course_fee.startswith("-") and base_course_fee[1:].isdigit():
        print("please input positive values only")
    elif base_course_fee.isdigit():
        base_course_fee = int(base_course_fee)
        if base_course_fee > 0:
            base_course_fee_valid = True
        else:
            print("please input non-zero value")
    else:
        print("enter only numbers")

# calculation of fee
discount = 0
print("enter description ")
description = input()
if description.lower().find("reference") != -1:
    discount += 5000

if "scholorship" in description:
    discount += 7000

if "promo" in description:
    discount += 3000

final_fee = base_course_fee - discount

print(f"base course fee {base_course_fee}")
print(f"you got discount {discount}")
print(f"after discount pay {final_fee}")