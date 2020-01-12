from client.Client import Client


if __name__ == "__main__":
    client = Client()

    client.set_proxy_address("142.93.72.206")
    client.set_proxy_port("3128")

    token = "1d10485eceee4565a2e2f51a4922e971"
    lang = 'ru'

    client.run(token, lang)
