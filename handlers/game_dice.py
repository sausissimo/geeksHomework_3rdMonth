from aiogram import types, Dispatcher
from config import bot
import random

async def game_dice(message: types.Message):
    games = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']
    chose_game = random.choice(games)

    await bot.send_message(chat_id=message.from_user.id, text="Bot's turn:")
    dice_bot = await bot.send_dice(chat_id=message.from_user.id, emoji=chose_game)
    await bot.send_message(chat_id=message.from_user.id, text="Your turn:")
    dice_user = await bot.send_dice(chat_id=message.from_user.id, emoji=chose_game)

    if dice_bot.values["dice"].value > dice_user.values["dice"].value:
        await bot.send_message(chat_id=message.from_user.id, text="Бот выиграл")
    elif dice_bot.values["dice"].value < dice_user.values["dice"].value:
        await bot.send_message(chat_id=message.from_user.id, text="Вы выиграли")
    else:
        await bot.send_message(chat_id=message.from_user.id, text="Ничья")


def register_game_dice(dp: Dispatcher):
    dp.register_message_handler(game_dice, commands=['game'])
