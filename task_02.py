import random


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return "Name: {}\nSurname: {}\nAverage score: {}\nCourses in progress: {}\nFinished courses: {}" \
            .format(self.name, self.surname, self.grades, self.courses_in_progress, self.finished_courses)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Error...'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):
    def __str__(self):
        return "Name: {}\nSurname: {}\nAverage score: {}".format(self.name, self.surname, self.grades)


class Reviewer(Mentor):
    def __str__(self):
        return "Name: {}\nSurname: {}".format(self.name, self.surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress and course in self.courses_attached:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error...'

# creating students Bo and Erin and attaching course/s to student
student_python = Student("Bo", "Chen", "male")
student_java = Student("Erin", "Meyer", "female")

student_python.courses_in_progress = ["Python", "Git"]
student_python.finished_courses = "Programming 101"

student_java.courses_in_progress = ["Java", "Git"]

# creating lecturer Dawn and Zuzana and attaching course/s
senior_lecturer = Lecturer("Dawn", "Casey")
regular_lecturer = Lecturer("Zuzana", "Krchova")

senior_lecturer.courses_attached = ["Python", "Java"]
regular_lecturer.courses_attached = ["Git"]

# rating lecturer¶
scores_lecturer_python = random.sample(range(6, 10), 4)
scores_lecturer_java = random.sample(range(6, 10), 4)
scores_lecturer_git = random.sample(range(6, 10), 4)

for score in scores_lecturer_python:
    student_python.rate_lecturer(senior_lecturer, "Python", score)

for score in scores_lecturer_java:
    student_java.rate_lecturer(senior_lecturer, "Java", score)

for score in scores_lecturer_git:
    student_java.rate_lecturer(regular_lecturer, "Git", score)
    student_python.rate_lecturer(regular_lecturer, "Git", score)

# creating reviewer Zanna and attaching course/s
junior_reviewer = Reviewer("Zanna", "Coldhawk")
junior_reviewer.courses_attached = ["Python", "Java"]


# rating homeworks of students
scores_student_python = random.sample(range(5, 10), 5)
scores_student_java = random.sample(range(5, 10), 5)

for score in scores_student_python:
    junior_reviewer.rate_hw(student_python, "Python", score)

for score in scores_student_java:
    junior_reviewer.rate_hw(student_java, "Java", score)

# Print result
print(student_python)
print(student_java)

print(senior_lecturer)
print(regular_lecturer)

# TODO
# "Как лучше реализовать подчет среднего, данный способ не работает?"

# class Lecturer2(Mentor):
#     grades = {'Python': [8, 8, 9], 'Java': [10, 9, 8]}
#
#     def avg_score(self):
#         total_score, count_score = 0
#
#         for key, value in self.grades:
#             total_score += sum(value)
#             count_score += len(value)
#
#         return "{:.2f}".format(total_score / count_score)
#
#     def __str__(self):
#         return "Name: {}\nSurname: {}\nAverage score: {}".format(self.name, self.surname, self.avg_score())
#
# senior_lecturer2 = Lecturer2("Dawn", "Casey")
# print(senior_lecturer2)

# TODO
"Как перенисти grades из класса Mentor в Lecturer?"

# TODO
"Не понятно что делать в задание №4"
