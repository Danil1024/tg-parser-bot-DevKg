from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb1 = KeyboardButton('/Начать_поиск')
kb2 = KeyboardButton('/Сбросить_все')

kb_help_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_help_client.add(kb1).add(kb2)