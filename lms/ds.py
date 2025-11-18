# student management system
system_info = ("lms students portal","v1.0","2025","edify university")
admin_info = ("admin@edify.ai","9440106595","201")

# display system info
print("="*50)
print(f"welcome to {system_info[0]}")
print(f"developed by {system_info[3]}")

# store with option selection
students = {}

# start with option selectio 
while True:
    print("choose an option from (1-5): ")
    print("1 - add student")
    print("2 - update student")
    print("3 - delete student")
    print("4 - list all students")
    print("s - exit system")

    choice = input("enter your choice: ")

    if choice =="1":
        print("performing operation 1")
        student_id = input("enter student id: ")

        # student exists
        if student_id in students:
            print("student already with this id exists in system")
        else:
            name = input("enter student name: ").title()

            # store multiple scores
            scores = []
            while True:
                score_input = input("enter a score or type done: ")

                # validate if input is number or done 
                if score_input == "done":
                    break
                if score_input.isdigit():
                    score = int(score_input)
                    if 0 <= score <=100:
                        scores.append(score)
                    else:
                        print("score should be between 0-100")
                else:
                    print("score should be number only")

            # store multiple skills 
            skills = set()
            while True:
                skill_input = input("enter a skill or type done: ") 
                if skill_input == "done":
                    break
                skills.add(skill_input.strip().title())   

            # save student details received so far
            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills
            }
            print("student added successfully! ")

            # for veridication print student
            print(students)


    elif choice == "2":
        print("perfoeming operation 2")
        # modify
        student_id = input("enter student id to modify: ")
        if student_id in students:
            new_name = input("enter new name to update: ").title()
            students[student_id]["name"] = new_name
            print("student updated successfully! ")
        else:
            print("student id doesn't exist")
        print(students)


    elif choice == "3":
        print("perfoeming operation 3")
        # delete
        student_id = input("enter student id to delete: ")
        removed = students.pop(student_id,None)
        if removed:
            print("student removed successfully")
        else:
            print("sudent id doesn't exist! ")
        print(students)


    elif choice == "4":
        print("perfoeming operation 4")
        # list all students
        if not students:
            print("no students available")
        else:
            print("="*50)
            print("student details ")
            print("="*50)

            for sid,data in students.items():
                name = data["name"]
                scores = data["scores"]

                if scores:
                    avg = sum(scores)/len(scores)
                else:
                    avg = 0
                    
                if scores:
                    top_scores = max(scores)
                else:
                    top_scores = 0

                skills = data["skills"]
                print(f"id: {id}")
                print(f"name: {name}")
                print(f"scores: {scores}")
                print(f"average score: {avg}")
                print(f"top score: {top_scores}")
                print(f"skills: {skills}")
                print(f"skills count: {len(skills)}")


    elif choice == "5":
        print("perfoeming operation 5")
        print("="*50)
        print("contact admin for future queries ")
        print(f"admin contac: {admin_info[1]}")
        print(f"admin email: {admin_info[0]}")
        print("="*50)

        break
    else:
        print("invalid choice only (1-5 available")
