from config import TOKEN
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import requests
from googletrans import Translator

bot = Bot(TOKEN)
dp = Dispatcher()
translator = Translator()

def get_advice():
    response = requests.get('https://api.adviceslip.com/advice')
    return response.json()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет, {message.from_user.full_name}! Сегодня я твой бот-советник!')

@dp.message(Command('advice'))
async def advice(message: Message):
    advice = get_advice()
    #en_advice = advice['slip']['advice']
    ru_advice = translator.translate(advice['slip']['advice'], dest='ru').text
    await message.answer(ru_advice)



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())