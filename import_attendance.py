from attendance import (initialize_attendance, mark_attendance, display_report,save_report)

students = ["Rosebud","Abnowel","George","Jonathan","Oye"]

MAX_DAYS = 30

while True:
    try:
        total_days = int(input("Enter the number of school days: "))

        if total_days < 1 or total_days > MAX_DAYS:
            print(f"Please enter a number between 1 and {MAX_DAYS}.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.")

attendance = initialize_attendance(students)

for day in range(total_days):
    print(f"\nDay{day + 1}")
    mark_attendance(students, attendance)

display_report(students, attendance, total_days)

save_report(students, attendance, total_days)