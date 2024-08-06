import logging
from config import dp, bot
from aiogram.utils import executor
from handlers import commands, echo, quiz, game_dice
from db import db_main
from aiogram import types

admin = [1208489667]

async def on_startup(_):
    for i in admin:
        await bot.send_message(chat_id=i, text='Бот включен!')
        await db_main.sql_create()


async def on_shutdown(_):
    for i in admin:
        await bot.send_message(chat_id=i, text='Бот выключен!')

commands.register_commands(dp)
quiz.register_quiz(dp)
game_dice.register_game_dice(dp)
echo.register_echo(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup,
                           on_shutdown=on_shutdown)