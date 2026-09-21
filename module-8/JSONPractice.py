import json
from pathlib import Path

# 1. Define the Student class
class Student:
    def __init__(self, F_Name, L_Name, Student_ID, Email):
        self.F_Name = F_Name
        self.L_Name = L_Name
        self.Student_ID = Student_ID
        self.Email = Email

    # Convert the class object back to a dictionary format for JSON saving
    def to_dict(self):
        return {
            "F_Name": self.F_Name,
            "L_Name": self.L_Name,
            "Student_ID": self.Student_ID,
            "Email": self.Email
        }

# 2. Define the print function
def print_student_list(students):
    """Loops through the student class list and prints out each value."""
    for student in students:
        print(
            f"First Name: {student.F_Name}, "
            f"Last Name: {student.L_Name}, "
            f"ID: {student.Student_ID}, "
            f"Email: {student.Email}"
        )
    print()  # Spacer line

# Use path object
file_path = Path("/Users/nee/Downloads/Student.json")

# =====================================================================
# STEP 1: Use the JSON load() function to load the file into a class list
# =====================================================================
with open(file_path, "r", encoding="utf-8") as file:
    raw_data = json.load(file)

student_list = [Student(**item) for item in raw_data]

# =====================================================================
# STEP 2 & 3: Output notification and call print function for original list
# =====================================================================
print("NOTIFICATION: This is the original Student list:\n")
print_student_list(student_list)

# =====================================================================
# STEP 4: Append new data to the class list
# =====================================================================
new_student = Student(
    F_Name="Neosha", 
    L_Name="Allen", 
    Student_ID=45715, 
    Email="neallen@my365.bellevue.com"
)
# Fixed: Added back the missing append function so the list actually changes
student_list.append(new_student)

# =====================================================================
# STEP 5 & 6: Output notification and call print function for updated list
# =====================================================================
print("NOTIFICATION: This is the updated Student list:\n")
print_student_list(student_list)

# =====================================================================
# STEP 7 & 8: Use JSON dump() to update the file and notify the user
# =====================================================================
updated_data = [student.to_dict() for student in student_list]

with open(file_path, "w", encoding="utf-8") as file:
    json.dump(updated_data, file, indent=4)

print("NOTIFICATION: The .json file was updated successfully!")