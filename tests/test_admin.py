import unittest
from src.admin.admin_tools import AdminTools

class TestAdminTools(unittest.TestCase):

    def setUp(self):
        self.admin_tools = AdminTools()

    def test_user_management(self):
        # Test adding a user
        self.admin_tools.add_user("test_user", "password123")
        self.assertIn("test_user", self.admin_tools.users)

        # Test removing a user
        self.admin_tools.remove_user("test_user")
        self.assertNotIn("test_user", self.admin_tools.users)

    def test_application_settings(self):
        # Test updating application settings
        self.admin_tools.update_settings({"theme": "dark"})
        self.assertEqual(self.admin_tools.settings["theme"], "dark")

if __name__ == '__main__':
    unittest.main()