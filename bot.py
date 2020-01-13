import logging

from aiogram import Bot, Dispatcher, executor, types
from ai_message import ai_message
API_TOKEN = 'TOKEN'
PROXY_URL = 'socks5://192.169.217.106:44659'  # Or 'socks5://host:port'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, proxy=PROXY_URL)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Hi, I'm SuperUserBot.\nI'm in the process of developing.")
