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

def calculate_percentage(attended_days, total_days):
    """Calculates attendance percentage"""
    if total_days == 0:
        return 0

    percentage = (attended_days / total_days) * 100
    return round(percentage)

def display_report(students, attendance, total_days):
    """Displays the attendance report"""
    print("\nATTENDANCE REPORT")
    print("=" * 40)

    for student in students:
        percentage = calculate_percentage(attendance[student], total_days)

        print(
            f"{student}: "
            f"{attendance[student]}/{total_days} days "
            f"({percentage}%)")


