import json
import os


class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def to_dict(self):
        return {
            "name": self.name,
            "student_id": self.student_id,
            "grade": self.grade
        }


class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):
        """Load data from file"""
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            return json.load(f)

    def save_students(self):
        """Save data to file"""
        with open(self.filename, "w") as f:
            json.dump(self.students, f, indent=4)

    def add_student(self, student):
        for s in self.students:
            if s["student_id"] == student.student_id:
                print(" Student ID already exists!")
                return
        self.students.append(student.to_dict())
        self.save_students()
        print(" Student added successfully.")

    def update_student(self, student_id, new_name, new_grade):
        for s in self.students:
            if s["student_id"] == student_id:
                s["name"] = new_name
                s["grade"] = new_grade
                self.save_students()
                print("Student updated successfully.")
                return
        print(" Student ID not found!")

    def delete_student(self, student_id):
        for s in self.students:
            if s["student_id"] == student_id:
                self.students.remove(s)
                self.save_students()
                print("Student deleted successfully.")
                return
        print(" Student ID not found!")

    def list_students(self):
        if not self.students:
            print("No student records found.")
            return
        print("\n=== Student Records ===")
        print(f"{'Name':<15} {'ID':<10} {'Grade':<10}")
        print("-" * 35)
        for s in self.students:
            print(f"{s['name']:<15} {s['student_id']:<10} {s['grade']:<10}")

def main():
    manager = StudentManager()

    while True:
        print("\n=== Student Management System ===")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. List Students")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            student_id = input("Enter ID: ")
            grade = input("Enter grade: ")
            student = Student(name, student_id, grade)
            manager.add_student(student)

        elif choice == "2":
            student_id = input("Enter ID to update: ")
            new_name = input("Enter new name: ")
            new_grade = input("Enter new grade: ")
            manager.update_student(student_id, new_name, new_grade)

        elif choice == "3":
            student_id = input("Enter ID to delete: ")
            manager.delete_student(student_id)

        elif choice == "4":
            manager.list_students()

        elif choice == "5":
            print("Goodbye ")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
