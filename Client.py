class Client:

    def __init__(self):
        self._message = None
        self._server = None

    def print_message(self):
        print(self._message)

    def set_message(self, message):
        self._message = message

    def set_server(self, server):
        self._server = server

    def run(self):
        self._server.set_message(self._message)
        self._server.run()
        self._message = self._server.get_answer()
