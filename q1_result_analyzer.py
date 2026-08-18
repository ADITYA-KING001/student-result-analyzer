def analyze_result(name, roll, marks):
    # Calculate total and average
    total = sum(marks)
    average = total / len(marks)

    # Assign grade
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    # Find subjects below 40
    failed_subjects = []

    for i in range(len(marks)):
        if marks[i] < 40:
            failed_subjects.append(f"Subject {i + 1}")

    # Display result
    print("Student:", name)
    print("Roll Number:", roll)
    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade)

    if failed_subjects:
        print("Subjects below 40:", ", ".join(failed_subjects))
    else:
        print("Subjects below 40: None")


# Student details
name = "Aarav"
roll = 101
marks = [88.5, 35.0, 76.0, 92.5, 48.0]

# Analyze result
analyze_result(name, roll, marks)
