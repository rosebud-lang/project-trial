#Attendance functions
def initialize_attendance(students):
    """Creates a dictionary with each student starting at 0 attendance days."""
    attendance = {}

    for student in students:
        attendance[student] = 0

    return attendance


