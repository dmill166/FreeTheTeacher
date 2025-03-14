import unittest
from src.gradebook.gradebook_manager import GradebookManager

class TestGradebookManager(unittest.TestCase):

    def setUp(self):
        self.gradebook = GradebookManager()

    def test_add_grade(self):
        self.gradebook.add_grade("student1", 90)
        self.assertEqual(self.gradebook.get_average("student1"), 90)

    def test_calculate_average(self):
        self.gradebook.add_grade("student1", 80)
        self.gradebook.add_grade("student1", 90)
        self.assertEqual(self.gradebook.get_average("student1"), 85)

    def test_generate_grade_report(self):
        self.gradebook.add_grade("student1", 70)
        self.gradebook.add_grade("student1", 80)
        report = self.gradebook.generate_grade_report("student1")
        self.assertIn("student1", report)
        self.assertIn("Average: 75.0", report)

if __name__ == '__main__':
    unittest.main()