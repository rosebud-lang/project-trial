# Mini-Project
Class Attendance Tracker

Introduction:

The Classroom Attendance Tracker is a Python-based application developed to assist in recording and managing students’ daily attendance. Attendance tracking is an essential task in educational settings because it provides valuable information about students’ participation and commitment to class activities. This project was designed for a fixed list of five students and demonstrates how programming can be applied to automate routine classroom management tasks. By using Python, the program records attendance, calculates attendance percentages, displays a summary report, and saves the report to a text file for future reference.

Project Description:

The main purpose of the Classroom Attendance Tracker is to simplify the process of recording daily attendance and generating attendance reports. The program prompts the user to enter the attendance status of each student for a given day. 
The program begins with a fixed list of five students. An attendance dictionary is then created, where each student's name is used as a key and their number of attended days is stored as the value.
For each school day, the program goes through the list of students one at a time and asks the user to enter whether each student is "Present" or "Absent". If a student is marked present, their attendance count increases by one. If the student is absent, their attendance count remains unchanged.
The program also includes input validation to ensure that only valid attendance responses are accepted. If the user enters an invalid response, such as a word other than "Present" or "Absent", the program displays an error message and asks for the information again instead of stopping unexpectedly.
The attendance data is then stored and updated over multiple days without losing previous records. At the end of the attendance recording process, the program calculates each student’s attendance percentage based on the formula:
(days attended / total days) × 100
The calculated percentages are rounded to produce clear and easy-to-read results. This allows teachers or users to quickly assess each student’s attendance performance.

Team Members:

This project was collaboratively developed by:
•	Abnowel Sam
•	Rosebud Awuah
The collaboration process involved planning the project structure, developing functions, testing the program, and ensuring that the final solution met the project requirements.

Features of the Program:

The Classroom Attendance Tracker includes several important features that enhance its functionality:
• Stores a fixed list of five student names.
• Creates an attendance record for every student.
• Records whether each student is present or absent.
• Tracks attendance over multiple school days.
• Maintains each student's attendance count without losing previous records.
• Calculates each student's attendance percentage.
• Rounds attendance percentages for easier reading.
• Displays a final attendance summary.
• Saves the final attendance report to a text file.
• Validates attendance input.
• Uses exception handling to reduce unexpected program crashes.
• Organizes the program into separate functions and modules

Technologies and Programming Concepts Used:

The project was developed using the following technologies and programming concepts:
•	Python: The primary programming language used to build the application.
•	Git: Used for version control and tracking changes during development.
•	GitHub: Used for collaboration and hosting the project repository.
•	Visual Studio Code (VS Code): Used as the integrated development environment for coding and testing.
In addition, the project demonstrates several core Python concepts, including:
•	Functions
•   Lists
•   Dictionaries
•   For loops
•   While loops
•	Conditional statements
•   User input using input()
•   String methods such as strip() and lower()
•   Exception handling using try and except
•   Raising errors using ValueError
•   File handling
•   Modules and imports
•   Percentage calculations
•   The round() function


Project Structure:

The project is organized into multiple files to improve clarity and maintainability. The main files include:
attendance.py: This file contains the main attendance functions used by the program.

The functions include:
- initialize_attendance() - creates an attendance dictionary and gives each student an initial attendance count of zero.
- mark_attendance() - goes through each student and asks whether the student is present or absent. It also validates the user's input.
- calculate_percentage() - calculates and rounds each student's attendance percentage.
- display_report() - displays the final attendance report on the screen.
- save_report() - saves the attendance report into a text file.


import_attendance.py: This is the main program file. It imports the functions from attendance.py and coordinates the running of the attendance tracker.
This is the main program file. It imports the functions from attendance.py and coordinates the running of the attendance tracker.

It contains the fixed list of five students and controls the overall flow of the program, including:

- setting up the student list
- initializing the attendance record
- receiving the total number of school days
- recording attendance for multiple days
- displaying the final report
- saving the report to a text file

•	attendance_report.txt: Stores the generated attendance report after the program is executed.
The report contains each student's:

- name
- number of days attended
- total number of school days
- attendance percentage

This file stores the final attendance report generated by the program.

•	README.md: Provides documentation and instructions for the project.


How to Run the Project:

To run the Classroom Attendance Tracker, the user should first clone the GitHub repository to their local machine. After opening the project folder in Visual Studio Code, the user should open the terminal and execute the command:
python3 import_attendance.py
The program will then prompt the user to enter the number of school days and the attendance status of each student. After all attendance data has been entered, the program will display a summary report and automatically generate the attendance_report.txt file.

