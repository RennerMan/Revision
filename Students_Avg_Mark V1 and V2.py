# Sorry, i forgot to make 2 copies for student avg mark for Q4&5. Hope that's ok! :D
max_mark = 0
total_marks = 0
num_students = 0
best_student = None
student_data = []

while True:
    student_name = input("Enter the student's name (or 'X' to quit): ")
    if student_name.upper() == 'X':
        break

    try:
        exam_mark = float(input("Enter the exam mark (0-100): "))
        if exam_mark < 0 or exam_mark > 100:
            raise ValueError("Mark must be between 0 and 100")
    except ValueError as e:
        print(e)
        continue

    def calculate_grade(mark):
        if mark >= 90:
            return 'A+'
        elif mark >= 85:
            return 'A'
        elif mark >= 80:
            return 'A-'
        elif mark >= 75:
            return 'B+'
        elif mark >= 70:
            return 'B'
        elif mark >= 65:
            return 'B-'
        elif mark >= 60:
            return 'C+'
        elif mark >= 55:
            return 'C'
        elif mark >= 50:
            return 'C-'
        elif mark >= 40:
            return 'D'
        else:
            return 'E'

    grade = calculate_grade(exam_mark)
    total_marks += exam_mark
    num_students += 1
    if exam_mark > max_mark:
        max_mark = exam_mark
        best_student = student_name

    student_data.append((student_name, exam_mark, grade))

if num_students > 0:
    average_mark = total_marks / num_students
    if best_student:
        print(f"The best student is {best_student} with a mark of {max_mark}.")
    else:
        print("No students entered.")
    print(f"The average mark for all students is {average_mark:.1f}.")

    print("Here is a list of all student names, marks, and grades")
    for student_name, exam_mark, grade in student_data:
        print(f"Name: {student_name}, Mark: {exam_mark}, Grade: {grade}")
else:
    print("No students entered.")

