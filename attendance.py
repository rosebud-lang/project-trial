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
            break
        elif status == "absent":
            pass
        else:
            print("Kindly enter Present or Absent.")

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

def save_report(students, attendance, total_days):
    """
    Saves the attendance report into a text file.
    """

    with open("attendance_report.txt", "w") as file:

        file.write("ATTENDANCE REPORT\n")
        file.write("=" * 40 + "\n")

        for student in students:

            percentage = calculate_percentage(
                attendance[student],
                total_days
            )
            file.write(
                f"{student}: "
                f"{attendance[student]}/{total_days} days "
                f"({percentage}%)\n"
            )

    print("\nReport successfully saved to attendance_report.txt")

