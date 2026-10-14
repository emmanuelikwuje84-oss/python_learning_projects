# Student Registration and Result Checker

## 1. Project Description

The Student Registration and Result Checker is a simple Python-based
application designed to manage student registration and calculate
examination results.

The system collects student information, validates examination scores,
assigns grades, determines pass or fail status, and generates a class
summary.

The project demonstrates the use of fundamental Python concepts to
solve a real-world problem through automation.

## 2. Features

The system provides the following features:

- Registers multiple students in one session.
- Collects each student's full name, registration number, department,
  and examination score.
- Validates examination scores to ensure they fall between 0 and 100.
- Assigns grades automatically according to predefined grading rules.
- Determines whether each student passed or failed.
- Displays individual student results.
- Allows users to continue registering students or end the session.
- Generates a class summary showing:
  - Total students processed.
  - Number of students who passed.
  - Number of students who failed.
  - Number of students who obtained grade A.

## 3. Technologies Used

- **Programming Language:** Python 3
- **Interface:** Command-line interface (CLI)
- **Development Concepts:** Variables, data types, strings, operators,
  conditions, loops, functions, user input, and output.

The application uses Python's built-in functionality and does not
require external libraries.

## 4. Project Structure

The project contains the following files:

    student_result_checker/
    ├── main.py
    └── README.md

- `main.py`: Contains the program logic, including student registration,
  score validation, grade calculation, result display, and class summary.
- `README.md`: Provides information about the project, its features,
  setup instructions, and usage.

## 5. Installation and Setup

### Requirements

- Python 3 installed on your computer.
- A terminal or command-line environment.

### Setup

1. Download or clone the project repository.
2. Open a terminal in the project directory.
3. Confirm that Python 3 is installed by running:

       python3 --version

No additional packages are required.

## 6. How to Run the Program

From the project directory, execute:

    python3 main.py

The welcome message will appear, and the system will begin the student
registration process.

## 7. How to Use the System

1. Start the application.
2. Enter the student's full name.
3. Enter the student's registration number.
4. Enter the student's department.
5. Enter the examination score as a whole number between 0 and 100.
6. Review the displayed grade and pass or fail result.
7. Choose whether to register another student by entering `yes` or `no`.
8. After registration ends, review the class summary.

If a score is outside the permitted range, the system requests another
score.

## 8. Grading System

The application uses the following grading rules:

| Score Range | Grade | Result |
|-------------|-------|--------|
| 70–100      | A     | Pass   |
| 60–69       | B     | Pass   |
| 50–59       | C     | Pass   |
| 45–49       | D     | Pass   |
| 40–44       | E     | Pass   |
| 0–39        | F     | Fail   |

A student passes with a score of 40 or above and fails with a score
below 40.

## 9. Limitations

The current version has the following limitations:

- Student records are not saved permanently. Information and summary
  counts are lost when the program closes.
- Registration numbers are not checked for duplicates.
- Non-numeric score input is not handled and may cause a program error.
- The system does not validate student names, registration numbers,
  or departments.
- The class summary provides only the statistics currently implemented.

## 10. Future Improvements

Possible improvements include:

- Saving student records to a file or database.
- Preventing duplicate registration numbers.
- Handling invalid and non-numeric input safely.
- Adding search functionality for registered students.
- Generating more detailed class performance reports.
- Developing a graphical user interface.

## 11. Author

Developed as a Python learning project to practise programming
fundamentals and apply them to a practical problem.