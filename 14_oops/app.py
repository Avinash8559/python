# instance variables
# instance methods
# class variables
# class methods
# local variables
# static methods
class Student:

    # class variables -- common for all objects
    institute_name = "digital edify"

    # instance variable -- __init__ : constructor
    def __init__(self,student_name,student_email):
        self.student_name = student_name
        self.student_email = student_email
    
    # instance method
    def info(self):
        print("welcome to: ",Student.institute_name)

        # instance level variables we use class name to access
        print("student name: ",self.student_name)
        print("student email: ",self.student_email)

    # class method
    def change_institute(cls,new_name):
        cls.institute_name = new_name

    #ststic method
    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email

student_one = Student("one","one@gmail.com")
student_two = Student("two","two@gmail.com")

Student.change_institute("digital lync")

print(Student.validate_email("one@gmail.com"))
print(Student.validate_email("two @gmail.com"))

student_one.info()
student_two.info()