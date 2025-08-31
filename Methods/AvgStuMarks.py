#def avg(name, marks):
    
student_data = {}
while True:
    roll_no = input("Enter roll number (or 'q' to quit): ")
    if roll_no.lower() == 'q':
        break
    name = input("Enter student name: ")
    marks_str = input("Enter marks (separated by a comma): ")
    marks = [int(mark) for mark in marks_str.split(',')]
    student_data[int(roll_no)] = (name, marks)

max_avg = 0
min_avg = float('inf')
max_student = None
min_student = None

for roll_no, (name, marks) in student_data.items():
    avg = sum(marks) / len(marks)
    if avg > max_avg:
        max_avg = avg
        max_student = (roll_no, name)
    if avg < min_avg:
        min_avg = avg
        min_student = (roll_no, name)

print("Student with highest average marks:", max_student)
print("Student with lowest average marks:", min_student)