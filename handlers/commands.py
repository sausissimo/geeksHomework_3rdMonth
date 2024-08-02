import os.path

from aiogram import types, Dispatcher
from aiogram.types import InputFile
from config import bot
import random

async def start_handler(message: types.Message):
    await message.answer(text="Hello!")

async def info_handler(message: types.Message):
    await message.answer("testbot1")

async def meme_handler(message: types.Message):
    path = "media/"
    files = []
    for f in os.listdir(path):
        full_path = os.path.join(path, f)
        if os.path.isfile(full_path):
            files.append(full_path)
    random_photo = random.choice(files)

    await message.answer_photo(photo=InputFile(random_photo))

async def message_handler(message: types.Message):
    if message.text.isdigit():
        x = int(message.text)
        x *= x
        await message.answer(x)
    else:
        await message.answer(message.text)


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=["start"])
    dp.register_message_handler(info_handler, commands=["info"])
    dp.register_message_handler(meme_handler, commands=["meme"])
    dp.register_message_handler(message_handler)
