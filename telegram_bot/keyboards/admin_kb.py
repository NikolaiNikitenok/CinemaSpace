# Кнопки админа 

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


mainAdmin = InlineKeyboardMarkup(row_width=2)
btnADD = InlineKeyboardButton(text="Загрузить", callback_data='btnADD')
btnDelete = InlineKeyboardButton(text="Удалить", callback_data='btnDelete')

mainAdmin.insert(btnADD).insert(btnDelete)

button_load = KeyboardButton('Загрузить⚙️')
button_delete = KeyboardButton('Удалить🗑')


button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).add(button_delete)
