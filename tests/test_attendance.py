import unittest
from src.attendance.attendance_tracker import AttendanceTracker

class TestAttendanceTracker(unittest.TestCase):

    def setUp(self):
        self.attendance_tracker = AttendanceTracker()

    def test_mark_attendance(self):
        self.attendance_tracker.mark_attendance('student1', '2023-10-01', True)
        self.assertTrue(self.attendance_tracker.get_attendance('student1', '2023-10-01'))

    def test_generate_attendance_report(self):
        self.attendance_tracker.mark_attendance('student1', '2023-10-01', True)
        report = self.attendance_tracker.generate_attendance_report('2023-10-01')
        self.assertIn('student1', report)

    def test_mark_multiple_attendance(self):
        self.attendance_tracker.mark_attendance('student1', '2023-10-01', True)
        self.attendance_tracker.mark_attendance('student1', '2023-10-02', False)
        report = self.attendance_tracker.generate_attendance_report('2023-10-01')
        self.assertIn('student1', report)

if __name__ == '__main__':
    unittest.main()