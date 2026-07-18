#Attendance functions
def initialize_attendance(students):
    """Creates a dictionary with each student starting at 0 attendance days."""
    attendance = {}

    for student in students:
        attendance[student] = 0

    return attendance


def mark_attendance(students, attendance):
    """Records attendance for one day"""
    print("\nMark Today's Attendance")
    print("-" * 30)

    for student in students:
        status = input(f"Is {student} Present or Absent? ").strip().lower()

        if status == "present":
            attendance[student] += 1


