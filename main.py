import asyncio
from aiogram import Bot, Dispatcher,types
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.filters import Command
from aiogram.enums import ParseMode
from api import TOKEN


bot = Bot(token=TOKEN,
parse_mode=ParseMode,html)
dp = Dispatcher()

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)")
inline_keyboard = 
main_keyboard.add (KeyboardButton("Привет!")), KeyboardButton"помощ
InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text="перейти на сайт,"url="hhtp;//example.com")]
InlineKeyboardButton(text="НАЖМИ",
callback_data="button_click")
])

@dp.message(lambda message; message.text == "привет")
async def hello(message; type.Message):
    await message.answer("привет,как дела",reply_markup=inline_keyboard)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("привет,я тестовый бот дамира",
    reply_markup=main_keyboard)

async def main():
    await dp.start_pollong(bot)

if _name_ == "_main_"
    asyncio.run(main())