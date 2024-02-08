
def main():
    # Initialize variables
    global best_student
    max_mark = 0
    total_marks = 0
    num_students = 0

    # Loop for input
    while True:
        student_name = input("Enter the student's name (or 'X' to quit): ")
        if student_name.upper() == 'X':
            break

        # Input validation for the exam mark
        try:
            exam_mark = float(input("Enter the exam mark (0-100): "))
            if exam_mark < 0 or exam_mark > 100:
                raise ValueError("Mark must be between 0 and 100")
        except ValueError as e:
            print(e)
            continue

        # Update variables
        total_marks += exam_mark
        num_students += 1
        if exam_mark > max_mark:
            max_mark = exam_mark
            best_student = student_name

    # Output results
    if num_students > 0:
        average_mark = total_marks / num_students
        print(f"The best student is {best_student} with a mark of {max_mark}.")
        print(f"The average mark for all students is {average_mark:.1f}.")
    else:
        print("No students entered.")
