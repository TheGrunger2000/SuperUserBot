from client.Client import Client
from server.Server import Server


if __name__ == "__main__":
    client = Client()
    server = Server()

    client.server = server
    token = "1d10485eceee4565a2e2f51a4922e971"
    lang = 'ru'

    client.run(token, lang)
