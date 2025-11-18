# functionality for multiple user types
class Person:
    def __init__(self,person_id,person_name,person_age):
        self.person_id = person_id
        self.person_name = person_name
        self.person_age = person_age

    def display_info(self):
        print("====info====")
        print(f"id: {self.person_id}")
        print(f"name: {self.person_name}")
        print(f"age: {self.person_age}")

# student - type of person
class Student(Person):
    def __init__(self,student_id,student_name,student_age):
        super().__init__(student_id,student_name,student_age)

# trainer - type of person, but has his own data also additionally
class Trainer(Person):
    def __init__(self,trainer_id,trainer_name,trainer_age,trainer_desc):
        super().__init__(trainer_id,trainer_name,trainer_age)
        self.trainer_desc = trainer_desc

    def display_info(self):
        super().display_info()
        print(f"description: {self.trainer_desc}")

# student
s1 = Student(101,"avi",20)
s1.display_info()

# trainer
t1 = Trainer(102,"ravi",40,"python instructer")
t1.display_info()