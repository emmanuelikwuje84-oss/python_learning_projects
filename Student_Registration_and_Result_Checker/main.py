# ==========================================
# STUDENT REGISTRATION AND RESULT CHECKER
# ==========================================


# SECTION 1: SCORE VALIDATION

def validate_score(score):
    if score >= 0 and score <= 100:
        return True
    else:
        return False


# SECTION 2: GRADE CALCULATION

def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"


# SECTION 3: PASS/FAIL CHECKING

def check_pass_status(score):
    if score >= 40:
        return True
    else:
        return False


# SECTION 4: DISPLAY STUDENT RESULT

def display_student_result(
    student_name,
    registration_number,
    department,
    score,
    grade,
    passed
):
    print("\n========== STUDENT RESULT ==========")
    print(f"Student Name: {student_name}")
    print(f"Registration Number: {registration_number}")
    print(f"Department: {department}")
    print(f"Score: {score}")
    print(f"Grade: {grade}")

    if passed:
        print("Result: PASS")
    else:
        print("Result: FAIL")

    print("====================================")


# SECTION 5: DISPLAY CLASS SUMMARY

def display_class_summary(
    total_students,
    passed_students,
    failed_students,
    grade_a_students
):
    print("\n========== CLASS SUMMARY ==========")
    print(f"Total students: {total_students}")
    print(f"Students who passed: {passed_students}")
    print(f"Students who failed: {failed_students}")
    print(f"Students who obtained grade A: {grade_a_students}")
    print("===================================")


# SECTION 6: MAIN PROGRAM

print("========================================")
print(" MOTHERLAND ACADEMY STUDENT REGISTRATION AND RESULT CHECKER")
print("========================================")
print("Welcome to the student result system!")


# Initialize summary counters

total_students = 0
passed_students = 0
failed_students = 0
grade_a_students = 0


# SYSTEM LOOP

continue_registration = "yes"

while continue_registration == "yes":

    print("\n--- Student Registration ---")

    # Collect student information

    student_name = input("Enter student's full name: ")
    registration_number = input("Enter registration number: ")
    department = input("Enter department: ")

    # Collect and validate the examination score

    score = int(input("Enter examination score: "))

    while not validate_score(score):
        print("Invalid score! Score must be between 0 and 100.")
        score = int(input("Enter examination score again: "))

    # Calculate grade and pass/fail status

    grade = calculate_grade(score)
    passed = check_pass_status(score)

    # Display the student's result

    display_student_result(
        student_name,
        registration_number,
        department,
        score,
        grade,
        passed
    )

    # Update summary counters

    total_students += 1

    if passed:
        passed_students += 1
    else:
        failed_students += 1

    if grade == "A":
        grade_a_students += 1

    # Ask whether to register another student

    continue_registration = input(
        "\nRegister another student? (yes/no): "
    ).strip().lower()


# SECTION 7: DISPLAY FINAL CLASS SUMMARY

display_class_summary(
    total_students,
    passed_students,
    failed_students,
    grade_a_students
)

print("\nThank you for using the student result system!")