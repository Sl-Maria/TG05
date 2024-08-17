from config import TOKEN

import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message #, FSInputFile, CallbackQuery
import requests
import random

bot = Bot(TOKEN)
dp = Dispatcher()

def get_answer():
    choices = ['yes', 'no', 'maybe']   #не нравится, что по умолчанию вариант maybe очень редкий
    choice = random.choice(choices)
    response = requests.get(f'https://yesno.wtf/api?force={choice}')
    return response.json()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет, {message.from_user.full_name}! '
                         f'\nЯ бот магический шар, который ответит на твои вопросы! '
                         f'\nПравда пока я умею отвечать только "да" или "нет"... зато с картинками!')

@dp.message()
async def reply(message: Message):
    answer = get_answer()
    img = answer['image']
    caption = answer['answer'].upper()
    await message.answer_animation(animation=img, caption=caption)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())