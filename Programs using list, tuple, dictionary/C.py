# Dictionary to store student details
gradebook = {}

def add_student(student_id, name):
    """Add a new student to the gradebook with an empty list for grades."""
    if student_id in gradebook:
        print("Student ID already exists.")
    else:
        gradebook[student_id] = {'name': name, 'grades': {}}
        print(f"Student '{name}' added successfully.")

def input_grades(student_id, subject, grade):
    """Input grades for a specific student and subject."""
    if student_id in gradebook:
        if subject in gradebook[student_id]['grades']:
            gradebook[student_id]['grades'][subject].append(grade)
        else:
            gradebook[student_id]['grades'][subject] = [grade]
        print(f"Grade {grade} added for {subject} to student ID {student_id}.")
    else:
        print("Error: Student ID not found.")

def view_grades(student_id):
    """Display the grades of a particular student for all subjects."""
    if student_id in gradebook:
        student = gradebook[student_id]
        print(f"\nGrades for {student['name']} (ID: {student_id}):")
        for subject, grades in student['grades'].items():
            print(f"Subject: {subject}, Grades: {grades}")
    else:
        print("Error: Student ID not found.")

def calculate_average(student_id):
    """Calculate the average grades for a particular student."""
    if student_id in gradebook:
        student = gradebook[student_id]
        total_grades = 0
        grade_count = 0
        for grades in student['grades'].values():
            total_grades += sum(grades)
            grade_count += len(grades)
        
        if grade_count > 0:
            average = total_grades / grade_count
            print(f"Average grade for {student['name']} (ID: {student_id}): {average:.2f}")
        else:
            print("No grades available to calculate the average.")
    else:
        print("Error: Student ID not found.")

def display_menu():
    """Display the menu options."""
    print("\nStudent Gradebook Management System")
    print("1. Add student")
    print("2. Input grades")
    print("3. View grades")
    print("4. Calculate average")
    print("5. Exit")

def main():
    print("Welcome to the Student Gradebook Management System")
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            add_student(student_id, name)
        
        elif choice == '2':
            student_id = input("Enter student ID: ")
            subject = input("Enter subject name: ")
            try:
                grade = float(input("Enter grade: "))
                if grade < 0:
                    raise ValueError("Grade must be a non-negative number.")
                input_grades(student_id, subject, grade)
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '3':
            student_id = input("Enter student ID: ")
            view_grades(student_id)
        
        elif choice == '4':
            student_id = input("Enter student ID: ")
            calculate_average(student_id)
        
        elif choice == '5':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
