class MessagingSystem:
    def __init__(self):
        self.messages = []

    def send_message(self, sender, recipient, content):
        message = {
            'sender': sender,
            'recipient': recipient,
            'content': content,
            'status': 'sent'
        }
        self.messages.append(message)
        return message

    def receive_messages(self, recipient):
        received_messages = [msg for msg in self.messages if msg['recipient'] == recipient]
        return received_messages

    def get_all_messages(self):
        return self.messages

    def delete_message(self, message_id):
        if 0 <= message_id < len(self.messages):
            del self.messages[message_id]
            return True
        return False