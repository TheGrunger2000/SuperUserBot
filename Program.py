from client.Client import Client
from server.Server import Server


if __name__ == "__main__":
    client = Client()
    server = Server()

    client.set_server(server)

    a = True
    while a:
        message = input("Enter Your Message\n>> ")

        client.set_message(message)
        client.run()
        client.print_message()

        while True:
            answer = input("Wanna do it some more? (y/n)\n>> ")

            if answer == "Y" or answer == "y":
                break

            elif answer == "N" or answer == "n":
                a = False
                break

            else:
                print("Error! Type \"Y\" or \"y\" or \"N\" or \"n\"")
