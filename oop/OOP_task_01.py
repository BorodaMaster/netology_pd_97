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
        return "\nName: {}\nSurname: {}\nAverage score: {:.2f}\nCourses in progress: {}\nFinished courses: {}" \
            .format(self.name, self.surname, sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), self.courses_in_progress, self.finished_courses)

    def __lt__(self, other):
        print("\n{} {} vs. {} {}".format(self.name, self.surname, other.name, other.surname))
        return sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])) < sum(sum(other.grades.values(), [])) / len(sum(other.grades.values(), []))

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
        return "\nName: {}\nSurname: {}\nAverage score: {:.2f}".format(self.name, self.surname, sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])))

    def __lt__(self, other):
        print("\n{} {} vs. {} {}".format(self.name, self.surname, other.name, other.surname))
        return sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])) < sum(sum(other.grades.values(), [])) / len(sum(other.grades.values(), []))


class Reviewer(Mentor):
    def __str__(self):
        return "\nName: {}\nSurname: {}".format(self.name, self.surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress and course in self.courses_attached:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error...'

def avg_hw_scope(course, students):
    scope = []
    count_scope = 0
    for student in students:
        if student.grades.get(course):
            scope += student.grades[course]
            count_scope += len(student.grades[course])

    return "Average scope homework {:.2f} for course {}".format(sum(scope) / count_scope, course)

def avg_lecture_scope(course, lecturers):
    scope = []
    count_scope = 0
    for lecturer in lecturers:
        if lecturer.grades.get(course):
            scope += lecturer.grades[course]
            count_scope += len(lecturer.grades[course])
    return "Average scope lecture {:.2f} for course {}".format(sum(scope) / count_scope, course)


## Creating classes and fill in data

# creating student/s Bo and Erin and attaching course/s to student
student_python = Student("Bo", "Chen", "male")
student_java = Student("Erin", "Meyer", "female")

student_python.courses_in_progress = ["Python", "Git"]
student_python.finished_courses = "Programming 101"

student_java.courses_in_progress = ["Java", "Git"]

# creating lecturer/s Dawn and Zuzana and attaching course/s
senior_lecturer = Lecturer("Dawn", "Casey")
regular_lecturer = Lecturer("Zuzana", "Krchova")

senior_lecturer.courses_attached = ["Python", "Java"]
regular_lecturer.courses_attached = ["Git", "Python"]

# rating lecturer
scores_regular_lecturer_python = random.sample(range(2, 10), 7)
scores_senior_lecturer_python = random.sample(range(6, 10), 4)
scores_lecturer_java = random.sample(range(6, 10), 4)
scores_lecturer_git = random.sample(range(2, 10), 6)

for score in scores_regular_lecturer_python:
    student_python.rate_lecturer(regular_lecturer, "Python", score)

for score in scores_senior_lecturer_python:
    student_python.rate_lecturer(senior_lecturer, "Python", score)

for score in scores_lecturer_java:
    student_java.rate_lecturer(senior_lecturer, "Java", score)

for score in scores_lecturer_git:
    student_java.rate_lecturer(regular_lecturer, "Git", score)
    student_python.rate_lecturer(regular_lecturer, "Git", score)

# creating reviewer/s Zanna and Hana and attaching course/s
junior_reviewer = Reviewer("Zanna", "Coldhawk")
junior_reviewer.courses_attached = ["Python", "Java"]

regular_reviewer = Reviewer("Hana", "Ticha")
regular_reviewer.courses_attached = ["Git"]

# rating homeworks of students
scores_student_python = random.sample(range(4, 10), 6)
scores_student_java = random.sample(range(5, 10), 5)
scores_student_git = random.sample(range(1, 10), 7)

for score in scores_student_python:
    junior_reviewer.rate_hw(student_python, "Python", score)

for score in scores_student_java:
    junior_reviewer.rate_hw(student_java, "Java", score)

for score in scores_student_git:
    regular_reviewer.rate_hw(student_python, "Git", score)
    regular_reviewer.rate_hw(student_java, "Git", score)


## Print result

# students
print(student_python)
print(student_java)

# lecturers
print(senior_lecturer)
print(regular_lecturer)

# reviewers
print(junior_reviewer)
print(regular_reviewer)

# compare students
print(student_python < student_java)

# compare lecturers
print(regular_lecturer < senior_lecturer)

# run functions
print()
# average homework scope by course
print(avg_hw_scope("Java", [student_python, student_java]))

# average lecture scope by course
print(avg_lecture_scope("Python", [regular_lecturer, senior_lecturer]))
