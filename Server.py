class Server:

    def __init__(self):
        self._message = None

    def set_message(self, message):
        self._message = message

    def get_answer(self):
        return self._message

    def run(self):
        if self._message == "Hello":
            self._message = "Dummy message"

        elif self._message == "How are you?":
            self._message = "How DARE you!"

        elif self._message == "Let's kill Java maybe?":
            self._message = "SURE!"

        else:
            self._message = "Nah, you're boring. Try again!"
