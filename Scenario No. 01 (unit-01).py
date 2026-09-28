# Student Management System using OOP

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.grade = self.assign_grade()

    # Assign grade based on marks
    def assign_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"

    # Display student details
    def display(self):
        print("Roll No :", self.roll_no)
        print("Name    :", self.name)
        print("Marks   :", self.marks)
        print("Grade   :", self.grade)
        print("------------------------")


class College:
    def __init__(self, college_name):
        self.college_name = college_name
        self.students = []

    # Add student object to college
    def add_student(self, student):
        self.students.append(student)

    # Display all students
    def display_students(self):
        print("\nCollege Name:", self.college_name)
        print("===== Student Details =====")

        for student in self.students:
            student.display()


# Create College object
college = College("ABC College")

# Create Student objects
student1 = Student(101, "Rahul", 85)
student2 = Student(102, "Priya", 92)
student3 = Student(103, "Amit", 67)
student4 = Student(104, "Sneha", 45)

# Add students to college
college.add_student(student1)
college.add_student(student2)
college.add_student(student3)
college.add_student(student4)

# Display all students
college.display_students()
