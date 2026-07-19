from attendance import (initialize_attendance, mark_attendance, display_report,save_report)

students = ["Rosebud","Abnowel","George","Jonathan","Oye"]

attendance = initialize_attendance(students)

total_days = 0

for day in range(total_days):
    print(f"\nDay{day + 1}")
    mark_attendance(students, attendance)

display_report(students, attendance, total_days)

save_report(students, attendance, total_days)