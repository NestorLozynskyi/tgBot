import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ParseMode
import os
from datetime import datetime, timedelta
import asyncio

API_TOKEN = '7699398565:AAG6gOT_9wgwO2MHAwGD5PT6ip6X6v-fh0w'
CHAT_ID = '@your_channel_or_group_id'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привіт! Я бот для автоматизації публікацій у групі Telegram.")

async def publish_post(content: str):
    try:
        await bot.send_message(chat_id=CHAT_ID, text=content, parse_mode=ParseMode.HTML)
    except Exception as e:
        logging.error(f"Помилка при публікації: {e}")

@dp.message_handler(commands=['post'])
async def schedule_post(message: types.Message):
    # Знімаємо команду /post і залишаємо тільки текст
    content = message.text[len('/post '):].strip()
    if content:
        await publish_post(content)
        await message.reply("Пост успішно опубліковано!")
    else:
        await message.reply("Будь ласка, надайте текст для публікації.")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
