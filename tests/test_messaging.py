import unittest
from src.messaging.messaging_system import MessagingSystem

class TestMessagingSystem(unittest.TestCase):

    def setUp(self):
        self.messaging_system = MessagingSystem()

    def test_send_message(self):
        result = self.messaging_system.send_message("parent@example.com", "Hello, this is a message.")
        self.assertTrue(result)
        self.assertIn("Hello, this is a message.", self.messaging_system.sent_messages)

    def test_receive_message(self):
        self.messaging_system.receive_message("teacher@example.com", "Important update.")
        self.assertIn("Important update.", self.messaging_system.received_messages)

    def test_message_history(self):
        self.messaging_system.send_message("parent@example.com", "First message.")
        self.messaging_system.send_message("parent@example.com", "Second message.")
        history = self.messaging_system.get_message_history("parent@example.com")
        self.assertEqual(len(history), 2)

if __name__ == '__main__':
    unittest.main()