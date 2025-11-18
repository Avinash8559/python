student_name = "Avi"
student_age = 22
student_id = 77
quiz_score = 75
assignment_score = 85
exam_score = 80
student_attendance = 65

#total score
total_score = quiz_score+assignment_score+exam_score

#average score
average_score = total_score/3

#student pass
student_pass = average_score >= 75

#attendance
student_attendance += 1 

#award
award_eligible=student_attendance >= 90 and student_pass

print(f"Student name: {student_name}")
print(f"Total score: {total_score}")
print(f"Average score: {average_score}")
print(f"Student passed: {student_pass}")
print(f"Student attendance: {student_attendance}")
print(f"Student awarded: {award_eligible}")