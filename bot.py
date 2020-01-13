# -*- coding: utf-8 -*-
import logging

from aiogram import Bot, Dispatcher, types, executor
API_TOKEN = 'TOKEN'
PROXY_URL = 'socks5://192.169.139.161:8975'  # Or 'socks5://host:port'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, proxy=PROXY_URL)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Hi, I'm SuperUserBot.\nI'm in the process of developing.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
