from aiogram import types, Dispatcher
from config import bot
import random

async def game_dice(message: types.Message):
    games = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']

    await bot.send_dice(chat_id=message.from_user.id, emoji=random.choice(games))


def register_game_dice(dp: Dispatcher):
    dp.register_message_handler(game_dice, commands=['game'])
