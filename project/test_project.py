import pytest
from io import StringIO
from project import calculate_attendance, display_attendance
import os
import sys

# Assume the functions are imported from project.py
# from project import calculate_attendance, display_attendance

# Example attendance data for testing
attendance_data = """
11/21/2024(Thu)	P	P	-	-	-	-
11/19/2024(Tue)	P	P	P	-	-	P
11/14/2024(Thu)	P	P	-	-	-	-
11/12/2024(Tue)	-	P	P	-	P	-
11/11/2024(Mon)	-	-	-	P	P	P
11/9/2024(Sat)	-	P	-	-	-	-
11/8/2024(Fri)	P	P	-	-	-	-
11/7/2024(Thu)	P	P	P	-	-	-
11/6/2024(Wed)	P	P	P	-	-	-
11/5/2024(Tue)	P	P	P	-	P	P
11/4/2024(Mon)	-	P	P	P	P	P
11/2/2024(Sat)	-	A	-	A	-	-
11/1/2024(Fri)	-	A	-	-	-	-
10/30/2024(Wed)	P	P	P	-	-	-
10/29/2024(Tue)	P	P	P	-	P	P
10/28/2024(Mon)	P	P	P	P	P	P
10/26/2024(Sat)	-	P	-	P	-	-
10/25/2024(Fri)	P	P	-	-	-	-
10/24/2024(Thu)	P	P	P	-	P	-
10/23/2024(Wed)	P	P	P	-	-	-
10/22/2024(Tue)	P	P	P	P	P	P
10/21/2024(Mon)	P	P	P	-	-	-
10/19/2024(Sat)	P	P	-	P	-	P
10/14/2024(Mon)	P	-	P	P	P	P
10/1/2024(Tue)	-	-	P	-	P	-
9/30/2024(Mon)	P	P	P	P	P	P
9/28/2024(Sat)	P	P	-	P	-	P
9/27/2024(Fri)	P	P	-	P	P	P
9/26/2024(Thu)	P	P	-	-	P	-
9/25/2024(Wed)	P	P	P	P	P	P
9/24/2024(Tue)	P	P	P	P	P	P
9/23/2024(Mon)	P	P	P	P	P	P
9/21/2024(Sat)	-	P	-	P	-	-
9/20/2024(Fri)	-	-	-	P	P	P
9/19/2024(Thu)	P	-	P	P	P	-
9/18/2024(Wed)	P	P	P	-	-	-
9/14/2024(Sat)	P	P	-	P	-	P
9/13/2024(Fri)	-	P	P	P	P	P
9/12/2024(Thu)	P	P	-	P	P	-
9/11/2024(Wed)	P	P	P	-	-	-
9/10/2024(Tue)	P	P	P	-	P	P
9/9/2024(Mon)	P	P	P	-	-	-
9/6/2024(Fri)	P	P	P	P	P	P
9/5/2024(Thu)	P	P	-	P	P	-
9/4/2024(Wed)	A	A	A	-	-	-
9/3/2024(Tue)	A	A	A	A	P	A
8/31/2024(Sat)	P	-	-	P	-	P
8/30/2024(Fri)	-	-	P	-	-	-
8/29/2024(Thu)	P	P	-	P	P	-
8/28/2024(Wed)	P	P	P	-	-	-
8/27/2024(Tue)	P	P	P	P	P	P
8/24/2024(Sat)	P	P	-	-	A	P
8/23/2024(Fri)	-	P	-	-	-	-
8/22/2024(Thu)	P	-	-	-	A	-
8/20/2024(Tue)	P	-	-	-	-	P
8/14/2024(Wed)	A	A	A	-	-	-
8/12/2024(Mon)	P	-	-	-	-	-
"""
# test input


def test_get_attendance_data():
    assert attendance_data == """
11/21/2024(Thu)	P	P	-	-	-	-
11/19/2024(Tue)	P	P	P	-	-	P
11/14/2024(Thu)	P	P	-	-	-	-
11/12/2024(Tue)	-	P	P	-	P	-
11/11/2024(Mon)	-	-	-	P	P	P
11/9/2024(Sat)	-	P	-	-	-	-
11/8/2024(Fri)	P	P	-	-	-	-
11/7/2024(Thu)	P	P	P	-	-	-
11/6/2024(Wed)	P	P	P	-	-	-
11/5/2024(Tue)	P	P	P	-	P	P
11/4/2024(Mon)	-	P	P	P	P	P
11/2/2024(Sat)	-	A	-	A	-	-
11/1/2024(Fri)	-	A	-	-	-	-
10/30/2024(Wed)	P	P	P	-	-	-
10/29/2024(Tue)	P	P	P	-	P	P
10/28/2024(Mon)	P	P	P	P	P	P
10/26/2024(Sat)	-	P	-	P	-	-
10/25/2024(Fri)	P	P	-	-	-	-
10/24/2024(Thu)	P	P	P	-	P	-
10/23/2024(Wed)	P	P	P	-	-	-
10/22/2024(Tue)	P	P	P	P	P	P
10/21/2024(Mon)	P	P	P	-	-	-
10/19/2024(Sat)	P	P	-	P	-	P
10/14/2024(Mon)	P	-	P	P	P	P
10/1/2024(Tue)	-	-	P	-	P	-
9/30/2024(Mon)	P	P	P	P	P	P
9/28/2024(Sat)	P	P	-	P	-	P
9/27/2024(Fri)	P	P	-	P	P	P
9/26/2024(Thu)	P	P	-	-	P	-
9/25/2024(Wed)	P	P	P	P	P	P
9/24/2024(Tue)	P	P	P	P	P	P
9/23/2024(Mon)	P	P	P	P	P	P
9/21/2024(Sat)	-	P	-	P	-	-
9/20/2024(Fri)	-	-	-	P	P	P
9/19/2024(Thu)	P	-	P	P	P	-
9/18/2024(Wed)	P	P	P	-	-	-
9/14/2024(Sat)	P	P	-	P	-	P
9/13/2024(Fri)	-	P	P	P	P	P
9/12/2024(Thu)	P	P	-	P	P	-
9/11/2024(Wed)	P	P	P	-	-	-
9/10/2024(Tue)	P	P	P	-	P	P
9/9/2024(Mon)	P	P	P	-	-	-
9/6/2024(Fri)	P	P	P	P	P	P
9/5/2024(Thu)	P	P	-	P	P	-
9/4/2024(Wed)	A	A	A	-	-	-
9/3/2024(Tue)	A	A	A	A	P	A
8/31/2024(Sat)	P	-	-	P	-	P
8/30/2024(Fri)	-	-	P	-	-	-
8/29/2024(Thu)	P	P	-	P	P	-
8/28/2024(Wed)	P	P	P	-	-	-
8/27/2024(Tue)	P	P	P	P	P	P
8/24/2024(Sat)	P	P	-	-	A	P
8/23/2024(Fri)	-	P	-	-	-	-
8/22/2024(Thu)	P	-	-	-	A	-
8/20/2024(Tue)	P	-	-	-	-	P
8/14/2024(Wed)	A	A	A	-	-	-
8/12/2024(Mon)	P	-	-	-	-	-
"""
# Test the function that calculates attendance


def test_calculate_attendance():
    present, absent, dash, plist, alist, hlist = calculate_attendance(attendance_data)

    assert present == 186
    assert absent == 16
    assert dash == 140

    # Check present days
    assert len(plist) == 50
    # Check absent days
    assert len(alist) == 4
    # Check half days
    assert len(hlist) == 3

# Test the function that displays attendance statistics


def test_display_attendance(capsys):
    present = 7
    absent = 4
    dash = 3
    plist = ["11/21/2024(Thu)\tP\tP\t-\t-\t-\t-", "11/14/2024(Thu)\tP\tP\t-\t-\t-\t-",
             "11/19/2024(Tue)\tP\tP\tP\t-\t-\tP", "11/12/2024(Tue)\t-\tP\tP\t-\tP\t-"]
    alist = ["11/11/2024(Mon)\t-\t-\t-\tP\tP\tP"]
    hlist = ["11/19/2024(Tue)\tP\tP\tP\t-\t-\tP"]

    # Capture the printed output
    display_attendance(present, absent, dash, plist, alist, hlist)

    # Get the captured output
    captured = capsys.readouterr()

    # Check for expected output in the captured text
    assert "Present classes= 7" in captured.out
    assert "Absent classes= 4" in captured.out
    assert "Not assigned classes= 3" in captured.out
    assert "Attendance = 63.64%" in captured.out  # Attendance for classes (7/(7+4))

    assert "Present days = 4" in captured.out
    assert "Absent days = 1" in captured.out
    assert "Half days = 1" in captured.out
    assert "Attendance = 83.33%" in captured.out  # Attendance for days (4 + 1) / (4 + 1 + 1)

# Test for edge case with empty data


def test_empty_data():
    str_data = ""
    present, absent, dash, plist, alist, hlist = calculate_attendance(str_data)

    assert present == 0, f"Expected 0 present classes, got {present}"
    assert absent == 0, f"Expected 0 absent classes, got {absent}"
    assert dash == 0, f"Expected 0 not assigned classes, got {dash}"
    assert len(plist) == 0, f"Expected 0 present days, got {len(plist)}"
    assert len(alist) == 0, f"Expected 0 absent days, got {len(alist)}"
    assert len(hlist) == 0, f"Expected 0 half days, got {len(hlist)}"

# Test for edge case with all present data


def test_all_present_data():
    str_data = """11/21/2024(Thu)\tP\tP\tP\tP\tP\tP
11/19/2024(Tue)\tP\tP\tP\tP\tP\tP"""

    present, absent, dash, plist, alist, hlist = calculate_attendance(str_data)

    assert present == 12, f"Expected 12 present classes, got {present}"
    assert absent == 0, f"Expected 0 absent classes, got {absent}"
    assert dash == 0, f"Expected 0 not assigned classes, got {dash}"

    # Check present days
    assert len(plist) == 2, f"Expected 2 present days, got {len(plist)}"
    assert len(alist) == 0, f"Expected 0 absent days, got {len(alist)}"
    assert len(hlist) == 0, f"Expected 0 half days, got {len(hlist)}"

# Test for edge case with all absent data


def test_all_absent_data():
    str_data = """11/21/2024(Thu)\tA\tA\tA\tA\tA\tA
11/19/2024(Tue)\tA\tA\tA\tA\tA\tA"""

    present, absent, dash, plist, alist, hlist = calculate_attendance(str_data)

    assert present == 0, f"Expected 0 present classes, got {present}"
    assert absent == 12, f"Expected 12 absent classes, got {absent}"
    assert dash == 0, f"Expected 0 not assigned classes, got {dash}"

    # Check absent days
    assert len(plist) == 0, f"Expected 0 present days, got {len(plist)}"
    assert len(alist) == 2, f"Expected 2 absent days, got {len(alist)}"
    assert len(hlist) == 0, f"Expected 0 half days, got {len(hlist)}"

# Test for mixed data


def test_mixed_data():
    str_data = """11/21/2024(Thu)\tP\tP\t-\t-\t-\t-
11/19/2024(Tue)\tA\tP\t-\tA\t-\tP
"""
    present, absent, dash, plist, alist, hlist = calculate_attendance(str_data)

    assert present == 4, f"Expected 4 present classes, got {present}"
    assert absent == 2, f"Expected 2 absent classes, got {absent}"
    assert dash == 6, f"Expected 6 not assigned classes, got {dash}"

    assert len(plist) == 1, f"Expected 1 present day, got {len(plist)}"
    assert len(alist) == 0, f"Expected 0 absent day, got {len(alist)}"
    assert len(hlist) == 1, f"Expected 1 half day, got {len(hlist)}"


# Run the tests
if __name__ == "__main__":
    pytest.main()
