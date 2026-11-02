# Student Marks Analysis System

import numpy as np
import pandas as pd

# Step 1: Create NumPy array of student marks
marks = np.array([85, 90, 75, 95, 60, 88, 78, 92])

# Step 2: Calculate statistical values
print("Student Marks:", marks)

print("Mean Marks:", np.mean(marks))
print("Median Marks:", np.median(marks))
print("Maximum Marks:", np.max(marks))
print("Minimum Marks:", np.min(marks))

# Step 3: Create student records
data = {
    'Name': ['Amit', 'Rahul', 'Sneha', 'Priya',
             'Rohan', 'Neha', 'Karan', 'Pooja'],
    'Marks': marks
}

# Step 4: Create Pandas DataFrame
df = pd.DataFrame(data)

print("\nStudent Records:")
print(df)

# Step 5: Display students scoring more than 80
print("\nStudents Scoring More Than 80 Marks:")
print(df[df['Marks'] > 80])
