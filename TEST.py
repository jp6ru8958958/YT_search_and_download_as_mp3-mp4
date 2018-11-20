class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


student = Student("ok", 100)
print(student.name, student.score)
