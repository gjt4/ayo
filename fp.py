import logging
import secrets
import string

from aiogram.types import Message
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5623424915:AAFLKsiLTCAMKYnsrhlliS_XMiWnryorWiw'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['generate_password'])
async def cmd_generate_password(message: Message):
    length = 16
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(chars) for i in range(length))
    await bot.send_message(chat_id=message.chat.id, text=f"Generated password: {password}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
