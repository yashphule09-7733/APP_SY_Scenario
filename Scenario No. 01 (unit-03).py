import csv
import argparse

# Accept filename using command-line argument
parser = argparse.ArgumentParser()
parser.add_argument("--file", required=True)
args = parser.parse_args()

filename = args.file

# Open CSV file
with open(filename, "r") as file:
    records = csv.DictReader(file)

    students = list(records)

# Display all student records
print("Student Records:")

for student in students:
    print(student)

# Search by Roll Number
roll = input("Enter Roll Number to search: ")

found = False

for student in students:
    if student["Roll Number"] == roll:
        print("Student Found:")
        print(student)
        found = True
        break

if not found:
    print("Student not found")
