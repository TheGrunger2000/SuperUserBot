import logging

from aiogram.types import ParseMode
from aiogram.utils.markdown import pre
from aiogram import Bot, Dispatcher, types, executor

from auth import get_setting
from ai_message import get_response, ai_message

API_TOKEN = get_setting('API Keys', 'telegram_bot_token')
PROXY_URL = get_setting('Proxy', 'url')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, proxy=PROXY_URL)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.chat.id,
                           "Hi, I'm SuperUserBot.\nI'm in the process of developing.")


@dp.message_handler(commands=['debug'])
async def send_debug_message(message: types.Message):
    try:
        debug_msg = get_response(message.text.replace('/debug'), '')
        await bot.send_message(message.chat.id, pre(debug_msg), parse_mode=ParseMode.MARKDOWN)
    except Exception as e:
        debug_msg = f'{e.__class__.__name__}: {e}'
        print(debug_msg)
        await bot.send_message(message.chat.id, f'{e.__class__.__name__}: {e}')


@dp.message_handler(commands=['bot'])
async def echo(message: types.Message):
    await bot.send_message(message.chat.id, ai_message(message.text.replace('/bot', '')))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
