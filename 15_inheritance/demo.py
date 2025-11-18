# without inheritance
class Student:

    # video functionality watching
    def watch_videos(self):
        print("="*50)
        print("functionality for watching videos")
        print("w")
        print("a")
        print("t")
        print("c")
        print("h")
        print("i")
        print("n")
        print("g")
        print("v")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print("="*50)

class VideoAdmin:
    # video functionality watching
    def watch_videos(self):
        print("="*50)
        print("functionality for watching videos")
        print("w")
        print("a")
        print("t")
        print("c")
        print("h")
        print("i")
        print("n")
        print("g")
        print("v")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print("="*50)

    # video functionality adding
    def add_videos(self):
        print("="*50)
        print("functionality for adding videos")
        print("a")
        print("d")
        print("d")
        print("i")
        print("n")
        print("g")
        print("v")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print("="*50)

class SuperAdmin:
    # video functionality watching
    def watch_videos(self):
        print("="*50)
        print("functionality for watching videos")
        print("w")
        print("a")
        print("t")
        print("c")
        print("h")
        print("i")
        print("n")
        print("g")
        print("v")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print("="*50)

    # video functionality adding
    def add_videos(self):
        print("="*50)
        print("functionality for adding videos")
        print("a")
        print("d")
        print("d")
        print("i")
        print("n")
        print("g")
        print("v")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print("="*50)

    # video functionality deleting
    def delete_videos(self):
        print("="*50)
        print("functionality for deleting videos")
        print("d")
        print("e")
        print("l")
        print("e")
        print("t")
        print("i")
        print("n")
        print("g")
        print("v")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print("="*50)

# test functionalities
print("student user")
student_user = Student()
student_user.watch_videos()

print("videoadmin user")
va_user = VideoAdmin()
va_user.watch_videos()
va_user.add_videos()

print("superadmin user")
sa_user = SuperAdmin()
sa_user.watch_videos()
sa_user.add_videos()
sa_user.delete_videos()


# with inheritance
class Student:

    # video functionality watching
    def watch_videos(self):
        print("="*50)
        print("functionality for watching videos")
        print("w")
        print("a")
        print("t")
        print("c")
        print("h")
        print("i")
        print("n")
        print("g")
        print("v")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print("="*50)

class VideoAdmin(Student):

    # video functionality adding
    def add_videos(self):
        print("="*50)
        print("functionality for adding videos")
        print("a")
        print("d")
        print("d")
        print("i")
        print("n")
        print("g")
        print("v")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print("="*50)

class SuperAdmin(VideoAdmin):

    # video functionality adding
    def add_videos(self):
        print("="*50)
        print("functionality for adding videos")
        print("a")
        print("d")
        print("d")
        print("i")
        print("n")
        print("g")
        print("v")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print("="*50)

    # video functionality deleting
    def delete_videos(self):
        print("="*50)
        print("functionality for deleting videos")
        print("d")
        print("e")
        print("l")
        print("e")
        print("t")
        print("i")
        print("n")
        print("g")
        print("v")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print("="*50)

# test functionalities
print("student user")
student_user = Student()
student_user.watch_videos()

print("videoadmin user")
va_user = VideoAdmin()
va_user.watch_videos()    # inherited from students
va_user.add_videos()

print("superadmin user")
sa_user = SuperAdmin()
sa_user.watch_videos()     # inherited from students
sa_user.add_videos()       # inherited from videoadmin
sa_user.delete_videos()