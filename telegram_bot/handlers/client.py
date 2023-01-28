from aiogram import types, Dispatcher
from create_bot import dp, bot
from data_base import sqlite_db

import keyboards.client_kb as nav
# --------------------------------------------------------------------------

# Переменные текста

mainTEXT = 'Привет!👋 Я CinemaSpace - Бот сообщества "КиноПространство".🎥\n\n \
🛋 Я помогу найти фильм или сериал по твоим вкусам!\n\n \
🌃 Ты сможешь подобрать фильмы на вечер или на выходные, \n \
для просмотра одному, в компании друзей или семьи!\n\n \
🌟 Можно посмотреть любимые жанры и фильмы знаменитостей.\n\n \
📔 Возможность найти фильм по коду, посмотрев отрезок в Тик-Ток.\n\n \
🎲 Можно выбрать случайный фильм для просмотра!'

CodeTEXT = 'Текст'

VIPTEXT = ''

RandomTEXT = ''

MyTEXT = ''

LinkTEXT = ''

SettingsTEXT = ''

StarTEXT = ''




# --------------------------------------------------------------------------
# @dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, text=mainTEXT, reply_markup=nav.mainMenu)
        await message.delete()
    except:
        await message.reply('Общение с ботом через Личные сообщения, напишите ему: \nhttp://t.me/CinemaSpaceSearch_bot')


# @dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Ты можешь воспользоваться командами: \n /start - "Запустить бота"\n /help - "Помощь" \n \
                           /films - "Посмотреть предложения"')


# @dp.message_handler(commands=['films'])
async def films_command(message: types.Message):
    await sqlite_db.sql_read(message)


# ------------------------------------------------


@dp.callback_query_handler(text="btnVIP")
async def vip(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Купи ВИП подписку!', reply_markup=nav.VIP)


@dp.callback_query_handler(text="btnVIPMore")
async def vipmore(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Ты получишь в ВИП подписке:', reply_markup=nav.VIPMore)


@dp.callback_query_handler(text="btnBackVIPMore")
async def backvipmore(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Купи ВИП подписку!', reply_markup=nav.VIP)


@dp.callback_query_handler(text="btnBackVIP")
async def backvip(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text=mainTEXT, reply_markup=nav.mainMenu)


@dp.callback_query_handler(text="btnLink")
async def link(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Подпишись на наши Соц. сети:', reply_markup=nav.Link)


@dp.callback_query_handler(text="btnBackLink")
async def backlink(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text=mainTEXT, reply_markup=nav.mainMenu)

@dp.callback_query_handler(text="btnCode")
async def code(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text=CodeTEXT, reply_markup=nav.Code)

#@dp.callback_query_handler(text="btnCodeSearch")

@dp.callback_query_handler(text="btnBackCode")
async def backcode(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, text=mainTEXT, reply_markup=nav.mainMenu)


# ----------------------------------------------

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(films_command, commands=['films'])
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
