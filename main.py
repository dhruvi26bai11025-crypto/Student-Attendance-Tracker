import csv

def save_data(students):
with open("attendance.csv", "w", newline="") as file:
writer = csv.writer(file)

writer.writerow(["Roll Number", "Name", "Present", "Total"])

for roll_no, student in students.items():
writer.writerow([
roll_no,
student["name"],
student["present"],
student["total"]
])

print("Attendance data saved successfully!")

def load_data():
students = {}

try:
with open("attendance.csv", "r", newline="") as file:
reader = csv.DictReader(file)

for row in reader:
students[row["Roll Number"]] = {
"name": row["Name"],
"present": int(row["Present"]),
"total": int(row["Total"])
}

print("Attendance data loaded successfully!")

except FileNotFoundError:
print("No previous attendance data found.")

return students

def add_student(students):
roll_no = input("Enter student roll number: ")

if roll_no in students:
print("Student already exists!")
return

name = input("Enter student name: ")

students[roll_no] = {
"name": name,
"present": 0,
"total": 0
}

print("Student added successfully!")

def mark_attendance(students):
roll_no = input("Enter roll number: ")

if roll_no not in students:
print("Student not found.")
return

status = input("Enter attendance (P for Present, A for Absent): ")

if status.upper() == "P":
students[roll_no]["present"] += 1
students[roll_no]["total"] += 1
print("Attendance marked as Present.")

elif status.upper() == "A":
students[roll_no]["total"] += 1
print("Attendance marked as Absent.")

else:
print("Invalid attendance status. Please enter P or A.")

def view_attendance(students):
print("\n===== ATTENDANCE RECORD =====")

if not students:
print("No students found.")
return

for roll_no, student in students.items():
if student["total"] > 0:
percentage = (student["present"] / student["total"]) * 100
else:
percentage = 0

print("Roll Number:", roll_no)
print("Name:", student["name"])
print("Classes Attended:", student["present"])
print("Classes Held:", student["total"])
print("Attendance Percentage:", round(percentage, 2), "%")
print("---------------------------------")

def low_attendance_report(students):
print("\n===== LOW ATTENDANCE REPORT =====")

found = False

for roll_no, student in students.items():
if student["total"] > 0:
percentage = (student["present"] / student["total"]) * 100

if percentage < 75:
print("Roll Number:", roll_no)
print("Name:", student["name"])
print("Attendance:", round(percentage, 2), "%")
print("Warning: Attendance is below 75%")
print("---------------------------------")
found = True

if not found:
print("No students have attendance below 75%.")

def show_menu():
print("\n===== STUDENT ATTENDANCE TRACKER =====")
print("1. Add Student")
print("2. Mark Attendance")
print("3. View Attendance")
print("4. Low Attendance Report")
print("5. Exit")

students = load_data()

while True:
show_menu()
choice = input("Enter the choice: ")

if choice == "1":
add_student(students)

elif choice == "2":
mark_attendance(students)

elif choice == "3":
view_attendance(students)

elif choice == "4":
low_attendance_report(students)

elif choice == "5":
save_data(students)
print("Thank you for using Student Attendance Tracker!")
break

else:
print("Invalid choice. Please try again.")