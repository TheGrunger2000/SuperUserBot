import configparser
import os


def create_config(path, tg_token, project_id, private_key_path, proxy_url):
    config = configparser.ConfigParser()
    config.add_section("API Keys")
    config.set("API Keys", "telegram_bot_token", tg_token)
    config.set("API Keys", "dialogflow_project_id", project_id)
    config.set("API Keys", "google_private_key_path", private_key_path)

    config.add_section("Proxy")
    config.set("Proxy", "url", proxy_url)

    with open(path, "w") as config_file:
        config.write(config_file)


def get_config(path):
    if not os.path.exists(path):
        auth(path)

    config = configparser.ConfigParser()
    config.read(path)
    return config


def get_setting(section, setting, path="bot_settings.ini"):
    config = get_config(path)
    value = config.get(section, setting)
    msg = f"{section}: {setting} is {value}"

    print(msg)
    return value


def auth(path):
    tg_token = input("Telegram Bot Token: ")
    project_id = input("Dialogflow Project ID: ")
    private_key_path = input("Google Private Key Path: ")
    proxy_url = input("Proxy Url: ")
    create_config(path, tg_token,
                  project_id, private_key_path, proxy_url)
    print("Сonfiguration file created!")
