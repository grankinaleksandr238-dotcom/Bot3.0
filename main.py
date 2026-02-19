import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "8579276360:AAG6zx6t2j5rQDhlZE0c3NkyABWAG0AOhts"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("✅ Бот работает! Привет!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
