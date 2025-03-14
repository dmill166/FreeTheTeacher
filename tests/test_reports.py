import unittest
from src.reports.report_generator import ReportGenerator

class TestReportGenerator(unittest.TestCase):

    def setUp(self):
        self.report_generator = ReportGenerator()

    def test_generate_attendance_report(self):
        # Assuming the method returns a report object or string
        report = self.report_generator.generate_attendance_report()
        self.assertIsNotNone(report)
        self.assertIn("Attendance Report", report)

    def test_generate_grade_report(self):
        # Assuming the method returns a report object or string
        report = self.report_generator.generate_grade_report()
        self.assertIsNotNone(report)
        self.assertIn("Grade Report", report)

    def test_generate_combined_report(self):
        # Assuming the method returns a report object or string
        report = self.report_generator.generate_combined_report()
        self.assertIsNotNone(report)
        self.assertIn("Combined Report", report)

if __name__ == '__main__':
    unittest.main()