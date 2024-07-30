class StudentGrades:
    def __init__(self):
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]

    def calculate_average(self, subject):
        if subject in self.grades:
            return sum(self.grades[subject]) / len(self.grades[subject])
        else:
            return 0

    def display_grades(self):
        for subject, grades in self.grades.items():
            average = self.calculate_average(subject)
            print(f"Subject: {subject}")
            print(f"Grades: {grades}")
            print(f"Average: {average:.2f}")
            print(f"Letter Grade: {self.letter_grade(average)}")
            print(f"GPA: {self.gpa(average)}")
            print()

    def letter_grade(self, average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def gpa(self, average):
        if average >= 90:
            return 4.0
        elif average >= 80:
            return 3.0
        elif average >= 70:
            return 2.0
        elif average >= 60:
            return 1.0
        else:
            return 0.0


def main():
    student_grades = StudentGrades()

    while True:
        print("1. Add Grade")
        print("2. Display Grades")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            subject = input("Enter subject: ")
            grade = float(input("Enter grade: "))
            student_grades.add_grade(subject, grade)
        elif choice == "2":
            student_grades.display_grades()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()
