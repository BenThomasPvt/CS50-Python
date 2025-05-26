# Attendance Overview
#### Video Demo:  [<URL HERE>](https://youtu.be/lZd9_VvBbdU)
#### Description:

Attendance Overview
Project Overview
Attendance Overview is a simple Python-based system for tracking attendance. It allows users to input daily attendance records for a set of students, then calculates and displays attendance statistics, such as the number of present and absent days, as well as overall attendance percentages for both classes and days. It's designed for ease of use and provides a clear summary of attendance data.

Features
Input Attendance Data: Users can enter attendance data line by line. Each line represents attendance for a specific day, with "P" for present, "A" for absent, and "-" for unassigned attendance.
Calculate Attendance: The program calculates the total number of present, absent, and unassigned days and classes.
Generate Report: The system displays a summary of:
Total present/absent classes
Overall class attendance percentage
Total present/absent/half days
Day-based attendance percentage
Files in the Project
1. project.py
Contains the main program logic with the following functions:
get_attendance_data(): Collects attendance data from the user.
calculate_attendance(): Processes the input data and computes attendance statistics.
display_attendance(): Displays the calculated statistics.
main(): Ties everything together and runs the program.
2. test_project.py
Includes unit tests using the pytest framework to validate the core functionality. The tests ensure the program handles different scenarios, including edge cases, and prints the correct output.
3. requirements.txt
Lists the required dependencies (currently just pytest for testing) to set up the project environment.
Design Choices
Input Method: I opted for manual line-by-line input to keep the system simple and flexible, allowing easy entry of attendance data.
Efficient Processing: Attendance is calculated in a single pass through the data to keep the program fast and responsive.
Clear Output: The statistics are displayed in a clear, easy-to-read format, making it simple for users to understand the results.
Testing: I used test-driven development to ensure the functions work as expected and handle edge cases, providing confidence in the system's reliability.
Future Enhancements
This project could be expanded with features like:

A graphical user interface (GUI) for easier input and display.
Exporting reports to CSV or Excel for further analysis.
Integration with online learning platforms to automate attendance tracking.
Conclusion
Attendance Overview is a straightforward, reliable tool for tracking attendance. It’s perfect for small-scale environments like classrooms, where simplicity and clarity are key. The program’s design prioritizes ease of use and accuracy, ensuring that you can quickly see the status of your attendance records.
