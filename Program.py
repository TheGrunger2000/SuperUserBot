from client.Client import Client
from server.Server import Server


if __name__ == "__main__":
    client = Client()
    server = Server()

    client.server = server
    token = "1d10485eceee4565a2e2f51a4922e971"
    lang = 'ru'

    a = True
    while a:
        message = input("Enter Your Message\n>> ")

        client.message = message
        client.run(token, lang)
        client.print_message()

        while True:
            answer = input("Wanna do it some more? (y/n)\n>> ")

            if answer == "Y" or answer == "y":
                break

            elif answer == "N" or answer == "n":
                a = False
                break

            else:
                print('Error! Type "Y" or "y" or "N" or "n')
