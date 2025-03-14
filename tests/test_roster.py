import unittest
from src.roster.roster_manager import RosterManager

class TestRosterManager(unittest.TestCase):

    def setUp(self):
        self.roster_manager = RosterManager()

    def test_add_student(self):
        self.roster_manager.add_student("John Doe")
        self.assertIn("John Doe", self.roster_manager.get_roster())

    def test_remove_student(self):
        self.roster_manager.add_student("Jane Doe")
        self.roster_manager.remove_student("Jane Doe")
        self.assertNotIn("Jane Doe", self.roster_manager.get_roster())

    def test_get_roster(self):
        self.roster_manager.add_student("Alice Smith")
        self.roster_manager.add_student("Bob Johnson")
        roster = self.roster_manager.get_roster()
        self.assertEqual(len(roster), 2)
        self.assertIn("Alice Smith", roster)
        self.assertIn("Bob Johnson", roster)

if __name__ == '__main__':
    unittest.main()