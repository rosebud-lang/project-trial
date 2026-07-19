#Attendance functions
# This function creates a dictionary for all students and sets each student's attendance count to zero.
def initialize_attendance(students):
    """Creates a dictionary with each student starting at 0 attendance days."""
    attendance = {}

    for student in students:
        attendance[student] = 0

    return attendance

# This function goes through each student and records whether the student is present or absent.

def mark_attendance(students, attendance):
    """Records attendance for one day"""
    print("\nMark Today's Attendance")
    print("-" * 30)

    for student in students:
        while True:
            try:
                status = input(f"Is {student} Present or Absent? ").strip().lower()

                if status == "present":
                    attendance[student] += 1
                    break

                elif status == "absent":
                    break

                else:
                    raise ValueError("Please enter only 'Present' or 'Absent'.")

            except ValueError as error:
                print(error)

# This function calculates and returns a student's attendance percentage based on the total number of days.

def calculate_percentage(attended_days, total_days):
    """Calculates attendance percentage"""
    if total_days == 0:
        return 0
    try:
        percentage = (attended_days / total_days) * 100
        return round(percentage)
    except ZeroDivisionError:
        return 0
    
#This function displays the final attendance report showing days attended and attendance percentage.

def display_report(students, attendance, total_days):
    """Displays the attendance report"""
    print("\nATTENDANCE REPORT")
    print("=" * 30)

    for student in students:
        percentage = calculate_percentage(attendance[student], total_days)

        print(
            f"{student}: "
            f"{attendance[student]}/{total_days} days "
            f"({percentage}%)")

#This function saves the final attendance report into a text file called attendance_report.txt.

def save_report(students, attendance, total_days):

    try:
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

    except OSError as error:
        print("An error occurred while saving the report.")
        print(error)
