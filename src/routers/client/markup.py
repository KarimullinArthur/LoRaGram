from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.dice import DiceEmoji


text_button_back = "Назад"

text_button_send_message = "📤Отправить сообщение"
text_button_update_name = "✏️Изменить имя"


def main_menu():
    send_message = KeyboardButton(text=text_button_send_message)

    keyboard = ReplyKeyboardMarkup(keyboard=[[send_message, ]], resize_keyboard=True)

    return keyboard


def back():
    back = KeyboardButton(text=text_button_back)

    keyboard = ReplyKeyboardMarkup(keyboard=[[back, ]], resize_keyboard=True)

    return keyboard
