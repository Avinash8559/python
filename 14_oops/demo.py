class Student:
    #student_name = "avi"
    #student_email = "avi@gmail.com"

    # __init__ special method
    def __init__(self,student_name,student_email):
        self.student_name = student_name
        self.student_email = student_email

    # custom method
    def info(self):
        print("student name: ",self.student_name)
        print("student email: ",self.student_email)

student_one = Student("one","one@gmail.com")
student_two = Student("second","second@gmail.com")
student_three = Student("third","third@gmail.com")

student_one.info()
student_two.info()
student_three.info()

    #def info(self):
        #print(self.student_name,self.student_email)
        #print(Student.student_name,Student.student_email)

#student_one = Student()
#student_one.info()

#student_two = Student()
#student_two.info()

