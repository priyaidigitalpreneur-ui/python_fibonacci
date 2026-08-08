
class Student:
    """Represents one student's personal information."""

    def __init__(self, full_name, age, address, student_id):
        # str: stores the student's full name as text.
        self.full_name = full_name
        # int: stores the student's age as a whole number.
        self.age = age

        # str: stores the student's address as text.
        self.address = address

        # str: stores the Student ID as text because IDs may contain
        # leading zeros or letters and should not be used for calculations.
        self.student_id = student_id

    def display(self):
        """Display the student's information."""
        print(f"Name: {self.full_name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Student ID: {self.student_id}")
        print("-" * 40)


class StudentManager:
    """Manages a collection of students."""

    def __init__(self):
        # list: stores multiple Student objects.
        # The list can contain 73 students or any other number of students.
        self.students = []

    def add_student(self, student):
        """Add a Student object to the student list."""
        self.students.append(student)

    def sort_by_age(self):
        """Sort students from youngest to oldest."""
        # The key parameter tells Python to use the student's age
        # when sorting the Student objects.
        self.students.sort(key=lambda student: student.age)

    def display_students(self):
        """Display all students."""
        for student in self.students:
            student.display()


def get_student_details():
    """Collect information for one student."""

    print("\nEnter student information")

    # input() returns a str (string) because names are text.
    full_name = input("Full Name: ").strip()

    # Convert the input string to int because age is a whole number.
    while True:
        try:
            age = int(input("Age: "))

            # Check that the age is a reasonable positive number.
            if age <= 0:
                print("Please enter a valid age.")
                continue

            break

        except ValueError:
            print("Please enter age as a whole number.")

    # str: addresses are stored as text.
    address = input("Address: ").strip()

    # str: Student IDs are stored as text so IDs such as "00123"
    # keep their leading zeros.
    student_id = input("Student ID: ").strip()

    # Create and return a Student object.
    return Student(full_name, age, address, student_id)


def main():
    """Main program."""

    # Create a StudentManager object to manage all students.
    manager = StudentManager()

    print("========================================")
    print("       STUDENT INFORMATION SYSTEM")
    print("========================================")
    print("Enter student details.")
    print("Enter 'q' when you have finished.\n")

    while True:
        # str: used to check whether the user wants to continue.
        choice = input(
            "Press Enter to add a student or type 'q' to finish: "
        ).strip().lower()

        if choice == "q":
            break

        # Create a Student object using the information entered by the user.
        student = get_student_details()

        # Add the Student object to the manager's list.
        manager.add_student(student)

    # Check whether any students were entered.
    if not manager.students:
        print("\nNo student information was entered.")
        return

    # Sort the students from youngest to oldest.
    manager.sort_by_age()

    print("\n========================================")
    print("       STUDENTS SORTED BY AGE")
    print("========================================")

    # Display the sorted students.
    manager.display_students()


# Program execution starts here.
if __name__ == "__main__":
    main()