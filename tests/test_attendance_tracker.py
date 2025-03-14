from FreeTheTeacher.src.attendance.attendance_tracker import AttendanceTracker, Student
from datetime import date

def test_attendance_tracker():
    tracker = AttendanceTracker(db_url='sqlite:///:memory:')  # Use in-memory DB for testing

    # Add a student
    session = tracker.Session()
    student = Student(name="John Doe")
    session.add(student)
    session.commit()
    student_id = student.id
    session.close()

    # Mark attendance
    tracker.mark_attendance(student_id, date(2025, 3, 13), present=True)
    tracker.mark_attendance(student_id, date(2025, 3, 14), present=False)

    # Get attendance
    attendance = tracker.get_attendance(student_id)
    assert attendance[date(2025, 3, 13)] is True
    assert attendance[date(2025, 3, 14)] is False

    # Generate attendance report
    report = tracker.generate_attendance_report()
    assert report[student_id]['name'] == "John Doe"
    assert report[student_id]['total_days'] == 2
    assert report[student_id]['days_present'] == 1
    assert report[student_id]['days_absent'] == 1