# memory.py
class Memory:
    def __init__(self):
        self.messages = []

    def add_message(self, role, content):
        self.messages.append({"role": role, "content": content})

    def get_messages(self):
        return self.messages

    def get_last_message(self, role):
        for message in reversed(self.messages):
            if message["role"] != role:
                return message["content"]
        return None

    def has_task_done(self):
        for message in self.messages:
            if "TASK_DONE" in message["content"]:
                return True
        return False