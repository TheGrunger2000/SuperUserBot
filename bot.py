# -*- coding: utf-8 -*-
import logging
from ai_message import ai_message

from aiogram import Bot, Dispatcher, types, executor
API_TOKEN = 'TOKEN'
PROXY_URL = 'socks5://192.169.214.83:37003'  # Or 'socks5://host:port'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, proxy=PROXY_URL)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Hi, I'm SuperUserBot.\nI'm in the process of developing.")


@dp.message_handler(commands=['d', 'bot'])
async def echo(message: types.Message):
    print(message.text)
    await message.answer(ai_message(message.text))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
